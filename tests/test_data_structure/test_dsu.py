import pytest
from data_structure.dsu import *
from random import *

class Test_Dsu():
    def test_init(self):
        size = randint(1, 10000)
        dsu = Dsu(size)
        assert(dsu.pa == list(range(size)))
    
    def test_find(self):
        size = randint(1, 10000)
        dsu = Dsu(size)
        assert(dsu.find(2) == 2)
    
    def test_union(self):
        size = randint(1, 10000)
        dsu = Dsu(size)
        dsu.union(2, 3)
        assert(dsu.find(2) == 3)
        

        
        