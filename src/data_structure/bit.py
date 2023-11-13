"""
树状数组

典型处理的问题是单点增加, 然后计算区间和
可以参考这个图片https://static.cdn.menci.xyz/oi-wiki/ds/images/fenwick.svg?h=GMr8Aw
总共会拆分出n个关键区间(n为数组的长度), 且关键区间的右端点各不相同
树状数组其实求的是一个前缀问题, 因为前缀和可以转化为区间和, 所以树状数组可以处理区间和
数组的下标从1开始
查询操作:
    如果需要查询nums[1]~nums[11]的区间和, 11 = 1011
    可以分解成求nums[1-8], nums[9-10], nums[11-11]的区间和
    每个区间长度都是2的幂
单点更新操作:
    如果需要更新nums[5], 因为是则需要更新树状数组[6]和树状数组[8]的位置
    5 = 101
    101+1 = 110
    110 + 10 = 1000
    每次都加上lowbit
"""
from typing import List
class BIT_SUM:
    def __init__(self, nums: List[int]):
        """初始化树状数组

        Args:
            nums (List[int]): 初始数组
        """
        n = len(nums)
        tree = [0] * (n+1)
        for i, num in enumerate(nums, 1):
            tree[i] += num
            nxt = i + (i & -i)
            if nxt <= n:
                tree[nxt]+=tree[i]
        self.tree = tree
        self.nums = nums

    def inc(self, index: int, k: int) -> None:
        """原数组下标为index的位置加上k

        Args:
            index (int): 需要加的位置
            k (int): 要加上的数
        """
        i = index+1
        while i < len(self.tree):
            self.tree[i] += k
            i += i & -i
        self.nums[index]+=k

    def sum(self, index: int) -> int:
        """  返回原数组[0, index]的元素和

        Args:
            index (int): 区间的右端点

        Returns:
            int: 闭区间[0, index]的区间和
        """
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def query(self, left: int, right: int) -> int:
        """
        返回原数组闭区间[left, right]的元素和

        Args:
            left (int): 区间的左端点
            right (int): 区间的右端点

        Returns:
            int: 区间和
        """
        return self.sum(right+1) - self.sum(left)