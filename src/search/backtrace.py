"""
回溯
回溯法是一种经常被用在 深度优先搜索(DFS) 和 广度优先搜索(BFS)的技巧。
其本质是：走不通就回头。
"""

"""
! 子集型回溯
分为子问题和原问题
需要思考三个问题:
当前操作是什么?
子问题是什么?
下一个子问题是什么
"""

"""
模板1: 集合的子集, 选和不选的问题
当前操作是什么? 枚举第i个数选不选
子问题是什么? 从下标>=i的数字中构造子集
下一个子问题是什么? 从下标>=i+1的数字中构造子集
典型题目: https://leetcode.cn/problems/subsets/
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            if i ==n:
                #! 一定要传复制进去, 不然其他的答案也会改变
                ans.append(path.copy())
                return
            #* 第i个元素不选
            dfs(i+1)
            #* 第i个元素选
            path.append(nums[i])
            dfs(i+1)
            #* 需要还原
            path.pop()
        dfs(0)
        return ans


"""
模板2: 集合的子集, 枚举下一个数要选谁
当前操作是什么? 枚举一个下标j>=i的数字, 加入path
子问题是什么? 从下标>=i的数字中构造子集
下一个子问题是什么? 从下标>=i+1的数字中构造子集
典型题目: https://leetcode.cn/problems/subsets/
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            ans.append(path.copy())
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans