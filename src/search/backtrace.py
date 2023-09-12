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
    
    
"""
! 组合型回溯
可以带剪枝操作
典型题型: https://leetcode.cn/problems/combinations/
时间复杂度为K*C(n, k), 也就是组合数* 数的高度
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(i):
            d = k - len(path)
            if(len(path)==k):
                ans.append(path.copy())
                return 
            #* 从后往前遍历
            #* 剪枝, 如果剩下的元素和当前路径不足以构成长度为k的就退出
            for j in range(i, d-1, -1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans
    

"""
! 组合型回溯
典型题型 https://leetcode.cn/problems/combination-sum-iii/
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(i, t):
            #* t表示剩余数字的和
            d = k - len(path)
            #* 剪枝, 如果剩余数字再选d个都达不到t, 或者t<0就跳过
            if(t < 0 or (i+i-d+1)*d//2 < t):
                return 
            if(len(path) == k and t == 0):
                ans.append(path.copy())
                return 
            for j in range(i, d-1, -1):
                path.append(j)
                dfs(j-1, t-j)
                path.pop()
        dfs(9, n)
        return ans
    
"""
! 组合型回溯
典型题型 https://leetcode.cn/problems/generate-parentheses/
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #! 可以看成是2n个位置中选n个位置填左括号, 剩下的填右括号
        #* 变成选或者不选的问题
        #* 左括号只要没到n个就可以填
        #* 右括号必须要当当前填了的左括号个数大于右括号才可以填
        path = []
        ans = []
        m = 2*n
        def dfs(i, open):
            if(i == m):
                ans.append(''.join(path))
                return 
            #* 可以填左括号
            if(open < n):
                path.append('(')
                dfs(i+1, open+1)
                path.pop()
            #* 可以填右括号
            if(i-open < open):
                path.append(')')
                dfs(i+1, open)
                path.pop()
        dfs(0, 0)
        return ans
            
                
        

                    