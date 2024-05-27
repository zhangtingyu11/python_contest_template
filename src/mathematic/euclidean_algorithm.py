"""
欧几里得算法, 可以通过辗转相除法来求gcd(a, b)
先看例子, a=38, b=28
a   b   mod
38  28  10
28  10  8
10  8   2
8   2   0
最后模出来是0, 具体可以看代码
"""
def gcd(a, b):
    while(b != 0):
        a, b = b, a%b
    return a