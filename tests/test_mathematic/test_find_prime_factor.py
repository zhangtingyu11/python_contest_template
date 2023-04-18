import unittest
from mathematic.find_prime_factor import *

class Test_TestFindPrimeFactor(unittest.TestCase):
    def test_find_prime_factor(self):
        n = 2**3 * 5**9 * 7**10
        self.assertListEqual(find_prime_factor(n), [2, 5, 7])
        
class Test_TestFindPrimeFactor(unittest.TestCase):
    def test_count_prime_factor(self):
        n = 2**3 * 5**9 * 7**10
        c = Counter({2:3, 5:9, 7:10})
        self.assertEqual(count_prime_factor(n), c)