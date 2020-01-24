from functools import reduce as _reduce

def encode(seq):
    """
    Encodes run-length encoding of given iterable.
    
    Parameters
    ----------
    seq: Any Python iterable, e.g.  lists, strings, tuples, 
        pandas Series, to perform run-length encoding on.
    
    Returns
    -------
    values, counts: list of contiguous unique values, and list of 
        counts 
    """
    assert len(seq) > 0, 'Sequence passed has zero length'
    
    values = []
    counts = []
    start_idxs = []
    end_idxs = []
    
    # First element
    values.append(seq[0])
    current_count = 1
    current_start_idx = 0
    
    for idx in range(1, len(seq)):
        # If the current value is the same as the last 
        # recorded unique value
        if seq[idx] == values[-1]:
            # Increment current count
            current_count += 1
        else:
            # Close previous count
            counts.append(current_count)
            start_idxs.append(current_start_idx)
            
            # Open new count 
            values.append(seq[idx])
            current_count = 1
            current_start_idx = idx

    # Close last count
    counts.append(current_count)
    start_idxs.append(current_start_idx)
    
    return values, counts


def mp_encode(seq, n_jobs=-1, n_chunks='auto', 
             backend='loky', verbose=1):
    
    """
    Parallelized version of `encode`.
    
    Parameters
    ----------
    seq: Any Python iterable, e.g.  lists, strings, tuples, 
        pandas Series, to perform run-length encoding on.
    n_jobs: Number of workers to parallelize, `n_jobs` parameter to be passed to joblib.Parallel. Defaults to -1.
    n_chunks: Number of chunks to split the input data into. Defaults to 'auto'.
    backend: Choice of backend for parallelization, `backend` parameter to be passed to joblib.Parallel. Defaults to 'loky'.
    verbose: Verbosity level, `verbose` parameter to be passed to joblib.Parallel. Defaults to 1.
    
    Returns
    -------
    values, counts: list of contiguous unique values, and list of 
        counts 
    """
    from joblib import Parallel, delayed
    import joblib

    # Automatically find best num of chunks to split data into
    # By using num of logical cores available
    if n_chunks == 'auto':
        n_chunks = joblib.cpu_count()
    
    # Split data into chunks
    # split_seq = np.array_split(seq, n_chunks)
    # Using np.array_split is convenient but it forces everything into the same data type! 
    # Preserving list homogeneity required a custom implementation that does not convert to np arrays.
    split_seq = _split(seq, n_chunks)
    
    # Parallelize `encode`
    output = Parallel(n_jobs=n_jobs, verbose=verbose,
    backend='loky')(map(delayed(encode), split_seq))
    
    # Gather outputs
    values, counts = [], []
    for i in output:
        values.extend(i[0])
        counts.extend(i[1])
        
    # Combine potential encodings that should be combined
    # But are separated as end of data chunks
    values, counts = _combine_values_counts(values, counts)    
    
    return values, counts

def _combine_values_counts(values, counts):
    new_values = []
    new_counts = []
    overflow_count = 0
    
    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            overflow_count = overflow_count + counts[i]
        else:
            new_values.append(values[i])
            new_counts.append(counts[i] + overflow_count)
            overflow_count = 0

    # Last value needs to be added manually
    # due to how the loop is set up
    new_values.append(values[-1])
    new_counts.append(counts[-1] + overflow_count)
            
    return new_values, new_counts

def _find_split_indices(length, n_chunks):
    # Calculate length of each chunk
    base_chunk_len = length // n_chunks
    overflow_len = length % n_chunks
    chunk_lengths = [base_chunk_len] * n_chunks
    
    for i in range(overflow_len):
        chunk_lengths[i] = chunk_lengths[i] + 1
        
    # Map out indices for each chunk
    # Note that num of cuts needed are n_chunks-1
    # cut_indices = [n1, n2, n3, n4, nn]
    # Last num is always the total length of the sequence
    cut_indices = [_reduce(lambda x, y: x+y, chunk_lengths[:i+1]) for i in range(n_chunks)]
    cut_indices.insert(0, 0)
    
    # Transform list of places to cut into proper list of indices
    split_indices = [slice(i, j) for i, j in zip(cut_indices[:-1], cut_indices[1:])]
    return split_indices

def _split(seq, n_chunks):
    split_indices = _find_split_indices(len(seq), n_chunks)
    split_seq = [seq[i] for i in split_indices]

    return split_seq

def decode(values, counts):
    """
    Decodes run-length encoding of given iterable.
    
    Parameters
    ----------
    values, counts: List of contiguous unique values, and list of counts
    
    Returns
    -------
    seq: Decoded sequence
    """
    assert len(values) == len(counts), 'len(values) != len(counts)'
    
    try:
        counts = [int(i) for i in counts]
    except:
        raise ValueError('Counts contain non-integer values')
    
    seq = [[i] * j for i, j in zip(values, counts)]
    seq = _reduce(lambda x, y: x + y, seq)
    return seq
        
    