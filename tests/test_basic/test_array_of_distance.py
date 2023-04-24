from basic.array_of_difference import *

def test_calculate_diff():
    nums = [1, 3, 6, 3, 5]
    assert calculate_diff(nums)==[1, 2, 3, -3, 2]

def test_calculate_origin_from_diff():
    diff = [1, 2, 3, -3, 2]
    assert calculate_origin_from_diff(diff) == [1, 3, 6, 3, 5]

def test_calculate_pre_sum_from_diff():
    diff = [1, 2, 3, -3, 2]
    assert calculate_pre_sum_from_diff(diff) == [1, 4, 10, 13, 18]

def test_calculate_changed_nums():
    nums = [1, 3, 6, 3, 5]
    changes = [[1, 3, 4],
               [0, 4, -1],
               [2, 2, 2]]
    assert(calculate_changed_nums(nums, changes)==[0, 6, 11, 6, 4])

    
def test_calculate_changed_nums_dim2():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    changes = [[1,1,2,2,1],[0,0,1,1,1]]
    ans = [[1, 1, 0],
           [1, 2, 1],
           [0, 1, 1]]
    assert(calculate_changed_nums_dim2(grid, changes)==ans)
    