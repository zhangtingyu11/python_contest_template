"""
树状数组

典型处理的问题是单点增加, 然后计算区间和
可以参考这个图片https://static.cdn.menci.xyz/oi-wiki/ds/images/fenwick.svg?h=GMr8Aw
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
class BIT:
    def __init__(self, n: int):
        """初始化树状数组

        Args:
            n (int): 如果原数组下标为0~n-1, 那么需要创建n+1长度的树状数组
        """
        self.tree = [0] * n

    def inc(self, i: int, k: int) -> None:
        """对下标为i的位置加上k

        Args:
            i (int): 需要加的位置
            k (int): 要加上的数
        """
        while i < len(self.tree):
            self.tree[i] += k
            i += i & -i

    def sum(self, i: int) -> int:
        """  返回闭区间 [1, i] 的元素和

        Args:
            i (int): 区间的右端点

        Returns:
            int: 闭区间 [1, i]的区间和
        """
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    def query(self, left: int, right: int) -> int:
        """
        返回闭区间 [left, right] 的元素和

        Args:
            left (int): 区间的左端点
            right (int): 区间的右端点

        Returns:
            int: 区间和
        """
        return self.sum(right) - self.sum(left - 1)