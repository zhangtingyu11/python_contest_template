"""
单调队列
用来处理窗口大小k的子数组的最值问题, 更一般的可以处理滑动窗口中的最值问题
如果要求最大值, 那么单调队列是单调递减的, 队首是最大值
如果要求最小值, 那么单调队列是单调递增的, 队尾是最小值
! 队列里面存的永远是索引
! 其实也可以求索引在一定范围内的某个东西的最值
"""

"""
例题以https://leetcode.cn/problems/sliding-window-maximum/description/ 为例
"""
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, num in enumerate(nums):
            #* 把里面<=当前元素的数弹出(其实只弹出小于的也可以)
            while(q and num>=nums[q[-1]]):
                q.pop()
            q.append(i)
            #* 如果队首的元素超过了长度为k的限制, 那么就要去掉
            if i-q[0]+1 > k:
                q.popleft()
            #* 只有在已经遍历了k个数之后才能将答案加进去
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans
                
"""
上面是一般情况
下面这题是依靠单调队列维护滑动窗口的最大最小值
https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
下面的关键点在于, 单调队列虽然具有单调性, 但是允许相同的元素进队(其实上面的例子也可以允许)
移动左指针的时候, 只要判断左指针是不是等于队首元素就可以判断最大值和最小值
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        ans = 0
        left = 0
        for right, num in enumerate(nums):
            while(max_q and num > nums[max_q[-1]]):
                max_q.pop()
            max_q.append(right)
            
            while(min_q and num < nums[min_q[-1]]):
                min_q.pop()
            min_q.append(right)
            
            #* 如果当前[left, right]区间的最大值和最小值差是>limit的, 左指针就需要右移
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > limit:
                if left == max_q[0]:
                    max_q.popleft()
                if left == min_q[0]:
                    min_q.popleft()
                left+=1
            ans = max(ans, right-left+1)
        return ans
            