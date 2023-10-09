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
