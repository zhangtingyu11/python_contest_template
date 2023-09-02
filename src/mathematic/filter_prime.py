"""
筛选质数, 可以在线性时间内筛选范围内的质数
"""

def filter_prime(n):
    primes = []
    is_prime = [True] * (n+1)
    for i in range(2, n+1):
        if(is_prime[i]):
            primes.append(i)
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return primes

