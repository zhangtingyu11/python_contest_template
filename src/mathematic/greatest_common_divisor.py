"""gcd
#! 最大公约数
"""
from typing import *
from math import *

"""
#! 给定一个数组nums, 如果快速求以下标i结尾的子数组的gcd的数目
考虑 2 6 3 4
假设要求的是f(i), 首先肯定要把第i个元素加进去
f(0): 就2一个元素
f(1): {2, 6}, 6和2求gcd得到2, 然后加上本身6
f(2): {1, 3}, 3和2求gcd得到1, 3和6求gcd得到3, 再加上本身3
f(3): {1, 4}, 4和1求gcd得到1, 4和3求gcd得到1, 再加上本身4
"""

def calculate_sub_array_gcd(nums: List[int])->List[int]:
    n = len(nums)
    ans = [0] * n
    s = set()
    
    for idx, num in enumerate(nums):
        ns = set()
        for item in s:
            ns.add(gcd(item, num))
        ns.add(num)
        ans[idx] = len(ns)
        s = ns
    return ans
