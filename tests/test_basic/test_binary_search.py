from basic.binary_search import *

def test_find_bigger_and_equal():
    nums = [1,2,3,3,4,5]
    assert(find_bigger_and_equal(nums, 3), 2)
    assert(find_bigger_and_equal(nums, 6), 6)
    
def test_find_bigger():
    nums = [1, 2, 4, 4, 5]
    assert(find_bigger(nums, 5)==5)
    assert(find_bigger(nums, 3)==2)
    
def test_find_smaller_and_equal():
    nums = [1, 2, 4, 4, 5]
    assert(find_smaller_and_equal(nums, 0)==-1)
    assert(find_smaller_and_equal(nums, 4)==3)
    
def test_find_smaller():
    nums = [1, 2, 4, 4, 5]
    assert(find_smaller(nums, 1)==-1)
    assert(find_smaller(nums, 4)==1)