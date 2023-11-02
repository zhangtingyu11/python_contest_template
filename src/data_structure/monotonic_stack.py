"""
单调栈: 具有单调性的栈结构, 用于处理下一个/上一个 更大/更小的数
单调栈里面存的是索引而不是值
"""

"""
例题可以参考https://leetcode.cn/problems/daily-temperatures/
![示意图](https://raw.githubusercontent.com/zhangtingyu11/PictureBed/main/202310071924234.png)
"""
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """从右往左看, 可以发现从右往左顺序是6 3 2 5, 那么当出现5之后2和3是无用的, 因为比2和3小的数一定比5小, 比2和3大的数的下一个更大的数也不可能是2和3
        因此可以发现单调栈必须是递减的

        Args:
            temperatures (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            #* 如果栈为空, 这里因为答案要求是0, 其他题目可以需要单独处理
            if st:
                ans[i] = st[-1]-i
            st.append(i)
        return ans

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """从左往右看, 如果数据是1 4 3 5, 那如果遇到了比栈顶大的数, 那栈顶元素的下一个更大的数一定是当前元素
        因此栈也要是递减的

        Args:
            temperatures (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            while st and t > temperatures[st[-1]]:
                last = st.pop()
                ans[last] = i-last
            #* 如果栈为空, 这里因为答案要求是0, 其他题目可以需要单独处理
            st.append(i)
        return ans 
    

"""
利用单调栈找到更大的数中最远的那个
https://leetcode.cn/problems/longest-well-performing-interval/
先将hour>8的设为1, hour<=8的设为-1, 求前缀和, 要找的是区间>0的最长区间
换句话说是枚举区间的左端点, 找到更大的距离它最远的点
或者枚举区间的右端点, 找到更小的距离它最远的点

考虑一个情况: 前缀和前面三个是8 3 6, 那么6可能作为左端点吗?
    不可能, 因为6能做左端点, 那么一定有个更大的区间以3为左端点
因此左端点的数值一定是单调递减的
然后因为要找最远的数, 所以右端点应该是从后往前遍历, 找到比它小的最前面的数
"""
from itertools import *
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums = [1 if hour > 8 else -1 for hour in hours]
        st = []
        pre_sm = list(accumulate(nums, initial=0))
        for idx, s in enumerate(pre_sm):
            if not st or s < pre_sm[st[-1]]:
                st.append(idx)
        ans = 0
        for right in range(len(pre_sm)-1, -1, -1):
            while st and pre_sm[right]>pre_sm[st[-1]]:
                ans = max(ans, right-st.pop())
        return ans

"""
换个思路, 枚举右端点
"""
from itertools import *
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums = [1 if hour > 8 else -1 for hour in hours]
        st = []
        pre_sm = list(accumulate(nums, initial=0))
        #* 变成维护单调递增的栈
        for i in range(len(pre_sm)-1, -1, -1):
            if not st or pre_sm[i] > pre_sm[st[-1]]:
                st.append(i)
        ans = 0
        for left in range(len(pre_sm)):
            while st and pre_sm[left] < pre_sm[st[-1]]:
                ans = max(ans, st.pop()-left)
        return ans

            
                
                
        
