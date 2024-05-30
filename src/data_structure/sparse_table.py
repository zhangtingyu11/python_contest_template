"""
ST表又称稀疏表, 主要用于解决可重复贡献问题
! 可重复贡献问题指的是对于指定的运算opt, 满足x opt x = x, 另外opt必须满足结合律才能被ST表求解, 并且ST表无法处理更新的问题
ST的思想是基于倍增的思想
以区间最大值为例, 令f(i, j)表示[i:i+2**j-1]这个区间里面的最大值
! 预处理
显然f(i, 0) = nums[i]
f(i, j) = max(f(i, j-1), f(i+2**(j-1), j-1))

! 查询
查询[l,r]的最大值, 可以拆解成max(f(l, s), f(r-2**s+1, s))
其中s = log(r-l+1)下取整
可以预处理log函数, log(1) = 0, log(i) = log(i//2) + 1
"""

class SparseTable:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        logn = [0] * (n+1)
        for i in range(2, n+1):
            logn[i] = logn[i//2]+1
        self.logn = logn
        self.build()
        
    def build(self):
        nums = self.nums
        n = len(nums)
        #* 最多会往后m次, 比如n=4, 初始是0, 0 + 2**2-1 = 3, 也就是会往后加2次, 下标是2, 长度就是3, 也就是n.bit_length()
        m = n.bit_length()
        dp = [[0] * (m) for _ in range(n)]
        for i in range(n):
            dp[i][0] = nums[i]
        for j in range(m):
            for i in range(n):
                #* 手写max函数会更快
                res1 = dp[i][j-1]
                res2 = dp[i+(1<<(j-1))][j-1]
                if res1 < res2:
                    dp[i][j] = res2
                else:
                    dp[i][j] = res1
        
        self.dp = dp
        
    def query(self, l, r):
        s = self.logn[r-l+1]
        mx = self.dp[l][s]
        if self.dp[r-(1<<s)+1][s] > mx:
            mx = self.dp[r-(1<<s)+1][s]
        return mx
        
        