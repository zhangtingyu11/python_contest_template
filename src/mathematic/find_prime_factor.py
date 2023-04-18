from typing import List
from collections import Counter
"""
#! 查找某个数n的质因数集合
#! 时间复杂度为O(logn)
"""


def find_prime_factor(n: int)->List[int]:
    """查找n的质因数构成的列表

    Args:
        n (int): 输入的数字n

    Returns:
        List[int]: 质因数构成的列表
    """
    i = 2
    primes = []
    while(i * i <= n):
        if(n % i == 0):
            primes.append(i)
            while(n % i == 0):
                n//=i
        i+=1
    if(n > 1):
        primes.append(n)
    return primes


def count_prime_factor(n: int)->Counter:
    """计算n的每个质因数的个数

    Args:
        n (int): 输入的数字n

    Returns:
        Counter: 质因数的计数器
    """
    i = 2
    primes = Counter()
    while(i * i <= n):
        while(n % i == 0):
            primes[i]+=1
            n//=i
        i+=1
    if(n > 1):
        primes[n]+=1
    return primes