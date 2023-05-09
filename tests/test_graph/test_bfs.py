from graph.bfs import *

def test_bfs_use_deque():
    assert bfs_use_deque([[1, 2], [0, 3], [0, 4, 5], [1], [2], [2]], 0)==2
    
def test_bfs_use_two_array():
    assert bfs_use_two_array([[1, 2], [0, 3], [0, 4, 5], [1], [2], [2]], 0)==2
    
def test_bfs_use_heap():
    assert bfs_use_heap([[1, 2], [0, 3], [0, 4, 5], [1], [2], [2]], 0, 4)==2