from random import *
from data_structure.bit import *

class TestBIT():
    def test_init(self):
        size = randint(1, 10000)
        bit = BIT(size)
        assert(bit.tree == [0] * size)
    
    def test_inc(self):
        size = 8
        bit = BIT(size+1)
        bit.inc(2, 3)
        assert(bit.tree == [0, 0, 3, 0, 3, 0, 0, 0, 3])
    
    def test_sum(self):
        size = 8
        bit = BIT(size+1)
        bit.inc(2, 3)
        assert(bit.sum(3) == 3)
        
    def test_query(self):
        size = 8
        bit = BIT(size+1)
        bit.inc(2, 3)
        bit.inc(3, 2)
        assert(bit.query(2, 3) == 5)