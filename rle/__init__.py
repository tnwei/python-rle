from tqdm import tqdm

def encode(iterable):
    """
    Encodes run-length encoding of given iterable.
    
    Parameters
    ----------
    iterable: Any Python iterable, e.g.  lists, strings, tuples, 
        pandas Series, to perform run-length encoding on.
    
    Returns
    -------
    values, counts, idxs: list of contiguous unique values, and list of 
        counts 
    
    """
    assert len(iterable) > 0, 'Iterable passed has zero length'
    
    values = []
    counts = []
    start_idxs = []
    end_idxs = []
    
    # First element
    values.append(iterable[0])
    current_count = 1
    current_start_idx = 0
    
    for idx in tqdm(range(1, len(iterable))):
        # If the current value is the same as the last 
        # recorded unique value
        if iterable[idx] == values[-1]:
            # Increment current count
            current_count += 1
        else:
            # Close previous count
            counts.append(current_count)
            start_idxs.append(current_start_idx)
            
            # Open new count 
            values.append(iterable[idx])
            current_count = 1
            current_start_idx = idx

    # Close last count
    counts.append(current_count)
    start_idxs.append(current_start_idx)
    
    return values, counts

"""
def mp_encode(iterable, 
             n_jobs=-1, n_chunks='auto', 
             backend='loky', verbose=0):
    # Use np.array_split() ???
    
    split_iterable = np.array_split(iterable, n_chunks)
    
    output = Parallel(n_jobs=n_jobs, verbose=verbose,
    backend='loky')(map(delayed(encode), split_iterable))
    
    for i in output:
        values.extend(i[0])
        counts.extend(i[1])
        
    return values, counts
"""
    