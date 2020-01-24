import rle

## Test rle.encode

def test_working():
    test_list = [1, 2, 2, 4, 4, 4, 5, 3]
    assert rle.encode(test_list) == ([1, 2, 4, 5, 3], [1, 2, 3, 1, 1])
    
def test_formats():
    test_tuples = (6, 6, 2, 2, 'abc', 3)
    assert rle.encode(test_tuples) == ([6, 2, 'abc', 3], [2, 2, 1, 1])
    
    test_string = 'aabbeeeeddsde'
    assert rle.encode(test_string) == (['a', 'b', 'e', 'd', 's', 'd', 'e'], [2, 2, 4, 2, 1, 1, 1])
    
def test_one_unique_value_only():
    test_list = [1]*50
    assert rle.encode(test_list) == ([1], [50])
    
def test_last_value_different():
    test_list = [1] * 49 + [2]
    assert rle.encode(test_list) == ([1, 2], [49, 1])