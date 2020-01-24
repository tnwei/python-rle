## Test rle.mp_encode
import rle

def test_mp_working():
    test_list = [1, 2, 2, 4, 4, 4, 5, 3]
    assert rle.mp_encode(test_list) == rle.encode(test_list), rle.mp_encode(test_list)
    
def test_mp_formats():
    test_tuples = (6, 6, 2, 2, 'abc', 3)
    assert rle.mp_encode(test_tuples) == rle.encode(test_tuples), rle.mp_encode(test_tuples)
    
    test_string = 'aabbeeeeddsde'
    assert rle.mp_encode(test_string) == rle.encode(test_string), rle.mp_encode(test_string)
    
def test_mp_one_unique_value_only():
    test_list = [1]*50
    assert rle.mp_encode(test_list) == rle.encode(test_list), rle.mp_encode(test_list)
    
def test_mp_last_value_different():
    test_list = [1] * 49 + [2]
    assert rle.mp_encode(test_list) == rle.encode(test_list), rle.mp_encode(test_list)