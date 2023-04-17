"""
#! 费马小定理
#! 参考: https://oi.wiki/math/number-theory/fermat/
#! 定义:
#!  若p为素数, gcd(a, p)=1, 则a^(p-1) mod p = 1
#!  另一种形式, 对于任意整数a 有a^p mod p = a mod p
"""

"""
#! 通过费马小定理求(a/b) mod p的值
#! (a/b) mod p = (a/b * 1) mod p
#!             = (a/b * b^(p-1)) mod p
#!             = (a*b^(p-2)) mod p
"""

def cal_a_div_b_mod_p(a, b, p):
    return (a * pow(b, p-2, p)) % p

def cal_a_div_b_mod_p_1(a, b, p):
    return (a * pow(b, -1, p)) % p
    