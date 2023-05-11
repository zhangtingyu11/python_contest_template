"""
#! 快速幂
我们需要计算x^n, 例如计算3^13
13可以表示成二进制1101
那我们只需要计算3^1, 3^4, 3^8即可, 可以只计算log个幂就可以得到结果
"""

def binpow(a:int, b:int)->int:
    """计算a^b

    Args:
        a (int): 底数
        b (int): 幂

    Returns:
        int: 结果
    """
    res = 1
    while b > 0:
        if (b & 1):
            res = res * a
        a = a * a
        b >>= 1
    return res

def binpow_mod_m(a:int, b:int, m:int)->int:
    """计算a^b mod m

    Args:
        a (int): 底数
        b (int): 幂
        m (int): 模

    Returns:
        int: 结果
    """
    a = a % m
    res = 1
    while b > 0:
        if (b & 1):
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

