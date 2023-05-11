from mathematic.fast_power import *

def test_binpow():
    assert(binpow(3,19) == pow(3, 19))
    
def test_binpow_mod_m():
    assert(binpow_mod_m(3, 19, 4) == pow(3, 19, 4))