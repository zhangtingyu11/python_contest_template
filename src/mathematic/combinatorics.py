"""
组合数学
"""

def comb(n, k, mod=10**9+7):
    """计算C(n, k)

    Args:
        n (_type_): 组合数的n值
        k (_type_): 组合数的k值
        mod (_type_, optional): 取模的对象. Defaults to 10**9+7.

    Returns:
        _type_: _description_
    """
    MOD = mod
    MX = n+1  #* 这个可以设置成题目给的数据范围的最大值

    #* 组合数模板, 一般下面的操作都放在预处理里面
    fac = [0] * MX
    fac[0] = 1
    for i in range(1, MX):
        fac[i] = fac[i - 1] * i % MOD

    inv_fac = [0] * MX  #* 求解阶乘的逆元
    inv_fac[MX - 1] = pow(fac[MX - 1], -1, MOD)
    for i in range(MX - 1, 0, -1):
        inv_fac[i - 1] = inv_fac[i] * i % MOD

    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


