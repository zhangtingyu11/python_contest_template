"""
#! 判断一个数是否是质数, 如果一个数只能被1和它自身整除, 那么这个数是质数, 最小的质数是2
#! 时间复杂度O(logn)
"""

def judge_prime(n: int)->bool:
    """判断一个数是不是质数

    Args:
        n (int): 输入的数

    Returns:
        bool: 如果是质数返回True, 否则返回False
    """
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            return False
        i+=1
    return n>=2