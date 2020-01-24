import rle

def test_working():
    values, counts = ['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 2, 1]
    assert rle.decode(values, counts) == ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e']
    
def test_formats():
    # Mixed formats
    values, counts = [6, 2, 'abc', 3], [2, 2, 1, 1]
    assert rle.decode(values, counts) == [6, 6, 2, 2, 'abc', 3]
    
    # All chars
    values, counts = ['a', 'b', 'e', 'd', 's', 'd', 'e'], [2, 2, 4, 2, 1, 1, 1]
    assert rle.decode(values, counts) == [i for i in 'aabbeeeeddsde']
    
def test_one_unique_value_only():
    values, counts = [1], [50]
    assert rle.decode(values, counts) == [1]*50
    
def test_one_value_only():
    values, counts = [1], [1]
    assert rle.decode(values, counts) == ([1])
    