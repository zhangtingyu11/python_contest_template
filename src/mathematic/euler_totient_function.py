"""
! 定义
欧拉函数, 可以求小于等于n的数中和n互质的数的个数
显然有# Math: \varphi(1)=1
当n是质数的时候, 显然有# Math: \varphi(n)=n-1

! 性质
欧拉函数是积性函数, 如果gcd(a,b)=1, 那么有# Math: \varphi(ab)=\varphi(a)\varphi(b)
特别地, 当n是奇数时, # Math: \varphi(2n)=\varphi(n)

如果# Math: n = p^k
其中p是质数, 那么# Math: \varphi(n)=p^k - p^{k-1}


如果# Math: n=\prod_{i=1}^{s}p_{i}^{k_{i}}
其中p_i是质数, 那么# Math: \varphi(n)= n\times\prod_{i=1}^{s}\frac{p_{i}-1}{p_{i}}
"""
import math

def euler_phi(n):
    """在枚举质因数的过程中, 计算欧拉函数的值

    Args:
        n (_type_): 输入数字
    """
    ans = n
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            ans = ans // i * (i-1)
            while n%i == 0:
                n //= i
        
    if n > 1:
        ans = ans // n * (n-1)
    return ans


"""
欧拉定理
如果gcd(a, m)=1, 那么# Math: a^{\varphi(m)}\equiv1\pmod{m}

拓展欧拉定理
# Math: a^b\equiv\begin{cases}a^{b\bmod\varphi(p)},&\gcd(a, p)=1\\a^b,&\gcd(a, p)\neq1, b<\varphi(p)\\a^{b\bmod\varphi(p)+\varphi(p)},&\gcd(a, p)\neq1, b\ge\varphi(p)\end{cases}\pmod{p}
需要注意的是, 如果p特别大, 用字符串表示, 那么可以先计算出m的欧拉函数值, 然后再慢慢处理b%m的欧拉函数值, 具体可以参考https://www.luogu.com.cn/problem/P5091
"""
    