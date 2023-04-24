from misc.discretization import *

def test_calculate_max_cnt_dim1():
    field = [[1,3], [2,4], [3, 6], [3,10**9]]
    assert(calculate_max_cnt_dim1(field)==4)
    
def test_calculate_max_cnt_dim2():
    forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]
    field = []
    for x, y, width in forceField:
        field.append([2*x-width, 2*y-width, 2*x+width, 2*y+width])
    assert(calculate_max_cnt_dim2(field)==3)