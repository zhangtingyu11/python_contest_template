"""
#! 同向双指针
同向双指针一般处理的是数组的最短子区间的问题
需要区间的长度具有单调性, 比如相同左端点情况下, 长度更长的子区间的和/积会比较长度较短的子区间的和/积要大(这需要数组的元素都是整数)

由于没有什么太套路的模板, 这里选取leetcode的例题说明
一般枚举是枚举右端点, 可以用enumerate来枚举端点位置和值

"""

"""
https://leetcode.cn/problems/minimum-size-subarray-sum/
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
from typing import List
from itertools import *
from math import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sm = 0
        left = 0
        ans = inf
        for right, num in enumerate(nums):
            sm += num
            while(sm-nums[left] >= target):
                sm -= nums[left]
                left+=1
            if(sm >= target):
                ans = min(ans, right-left+1)
        return ans if ans < inf else 0
    
    
"""
相向双指针
可以用来判断有序数组中有没有两个元素的和等于target

#!要点就是有序数组
没有什么太套路的模板, 选择leetcode的例题进行说明
"""

"""
https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
167. 两数之和 II - 输入有序数组

给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
你所设计的解决方案必须只使用常量级的额外空间。

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 非递减顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while(left < right):
            s = numbers[left]+numbers[right]
            if(s < target):
                left+=1
            elif(s > target):
                right-=1
            else:
                return [left+1, right+1]

                

