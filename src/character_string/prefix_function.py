"""
计算字符串的前缀函数
pi[i]表示子串s[0:i]最长的相等的真前缀与真后缀的长度
定义pi[0] = 0
"""

def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi