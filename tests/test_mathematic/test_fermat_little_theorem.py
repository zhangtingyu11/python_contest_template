import unittest
from mathematic.fermat_little_theorem import *
from math import factorial
from random import *

class Test_TestCalADivBModP(unittest.TestCase):
    def test_cal_a_div_b_mod_p(self):
        m = randint(1, int(1e5))
        n = randint(1, int(1e5))
        mx = max(m, n)
        mn = min(m, n)
        MOD = 10**9+7
        self.assertEqual(cal_a_div_b_mod_p(factorial(mx), factorial(mn), MOD), (factorial(mx)//factorial(mn))%MOD)
    
class Test_TestCalADivBModP1(unittest.TestCase):
    def test_cal_a_div_b_mod_p1(self):
        m = randint(1, int(1e5))
        n = randint(1, int(1e5))
        mx = max(m, n)
        mn = min(m, n)
        MOD = 10**9+7
        self.assertEqual(cal_a_div_b_mod_p_1(factorial(mx), factorial(mn), MOD), (factorial(mx)//factorial(mn))%MOD)
        