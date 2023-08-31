"""
数位dp
数位是指把一个数字按照个、十、百、千等等一位一位地拆开，关注它每一位上的数字。如果拆的是十进制数，那么每一位数字都是 0~9,其他进制可类比十进制。

数位 DP:用来解决一类特定问题,这种问题比较好辨认,一般具有这几个特征：

1.要求统计满足一定条件的数的数量（即，最终目的为计数）；

2.这些条件经过转化后可以使用「数位」的思想去理解和判断；

3.输入会提供一个数字区间（有时也只提供上界）来作为统计的限制；

4.上界很大（比如 10^{18}），暴力枚举验证会超时。

以https://leetcode.cn/problems/count-special-integers/为例讲下数位dp的模板
"""
from functools import cache
def getRes(num):
    s = str(num)
    @cache
    def dfs(i:int , mask:int, is_limit:bool, is_num:bool)->int:
        """数位dp

        Args:
            i (int): 从i开始填数组
            mask (int): i前面填的数字的集合是mask
            is_limit (bool): 表示前面填的数字是否都是n对应位上的, 如果为true, 那么当前位至多为int(s[i]), 否则至多为9
            is_num (bool): 表示前面是否填了数字(是否跳过), 如果为true, 那么当前位可以从0开始, 如果为false, 那么可以跳过或者从1开始填数字

        Returns:
            int: 满足条件的数字个数
        """
        if(i == len(s)):
            return int(is_num) 
        res = 0
        if not is_num:  #* 选择跳过数字
            res = dfs(i+1, mask, False, False)
            
        up = int(s[i]) if is_limit else 9
        for d in range(1- int(is_num), up+1):
            if mask >> d & 1 == 0: #* mask里面没有d
                res += dfs(i+1, mask|(1<<d), is_limit and d==up, True)
        return res
    return dfs(0, 0, True, False)


