import unittest
from mathematic.judge_prime import *

class Test_TestJudgePrime(unittest.TestCase):
    def test_judge_prime0(self):
        n = 2**3
        self.assertFalse(judge_prime(n), False)
        
    def test_judge_prime1(self):
        n = 1
        self.assertFalse(judge_prime(n))
        
    def test_judge_prime2(self):
        n = 13
        self.assertTrue(judge_prime(n))
        
    def test_judge_prime3(self):
        n = 2
        self.assertTrue(judge_prime(n))