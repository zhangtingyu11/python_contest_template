"""
#! 线段树
https://oi.wiki/ds/seg/
可以多维护一些区间来进行单点/区间修改和查询
"""

"""
单点修改+区间查询
"""
from typing import List

class SegmentTreeSingleModifyAdd:
    """线段树单点增加, 区间求和, 可以用树状数组平替
    """
    def __init__(self, n: int, nums: List[int]) -> None:
        """初始化线段树类

        Args:
            n (int): 初始数组的长度
            nums (List[int]): 初始的数组
        """
        self.sm = [0] * (n*4)
        self.nums = nums
        self.build(1, 1, n)
        
    def build(self, o: int, l: int, r: int)->None:
        """构建[l, r]内的线段树

        Args:
            o (int): 当前的节点编号
            l (int): 要构建的区间的左端点
            r (int): 要构建的区间的右端点
        """
        if l == r:  #* 如果左右端点相等, 说明是叶子节点, 直接赋值即可
            #* 因为l的范围是[1, n], 所以作为数组的索引时需要减一
            self.sm[o] = self.nums[l-1]
            return
        
        #* 否则需要递归遍历左右子树
        mid = (l+r)//2
        self.build(o*2, l, mid)
        self.build(o*2+1, mid+1, r)
        self.sm[o] = self.sm[o*2] + self.sm[o*2+1]
        
    #* 具体操作就是add[1, 1, n, idx, val], 前面三个参数是不变的
    def add(self, o: int, l: int, r: int, idx: int, val: int)->None:
        """在idx位置增加val
        #! 需要注意的是idx的范围是[1, n]并不是从0开始

        Args:
            o (int): 当前的节点编号
            l (int): 当前的节点所对应的区间左端点
            r (int): 当前的节点所对应的区间右端点
            idx (int): 需要增加值的位置, 注意范围是[1, n]
            val (int): 需要增加的值
        """
        if l == r:
            self.sm[o]+=val
            return
        
        mid = (l+r)//2
        #* 需要判断idx在左右哪个区间内
        if(idx <= mid):
            self.add(o*2, l, mid, idx, val)
        else:
            self.add(o*2+1, mid+1, r, idx, val)
        self.sm[o] = self.sm[o*2] + self.sm[o*2+1]
    
    
    #* 具体操作就是query_sum[1, 1, n, L ,R], 前面三个参数是不变的
    def query_sum(self, o: int, l: int ,r: int, L: int, R: int)->int:
        """求[L, R]的区间和

        Args:
            o (int): 当前的节点编号
            l (int): 当前节点所对应的区间的左端点
            r (int): 当前节点所对应的区间的右端点
            L (int): 查询的区间的左端点
            R (int): 查询的区间的右端点

        Returns:
            int: 区间和
        """
        if L<=l and R>=r:
            return self.sm[o]

        sm = 0
        mid = (l+r)//2
        if(L <= mid):
            sm += self.query_sum(o*2, l, mid, L, R)
        if(R > mid):
            sm += self.query_sum(o*2+1, mid+1, r, L, R)
        return sm

from math import * 

class SegmentTreeSingleModifyMax:
    """线段树单点更新, 区间求最大值
    """
    def __init__(self, n: int, nums: List[int]) -> None:
        """初始化线段树类

        Args:
            n (int): 初始数组的长度
            nums (List[int]): 初始的数组
        """
        self.mx = [-inf] * (n*4)
        self.nums = nums
        self.build(1, 1, n)
        
    def build(self, o: int, l: int, r: int)->None:
        """构建[l, r]内的线段树

        Args:
            o (int): 当前的节点编号
            l (int): 要构建的区间的左端点
            r (int): 要构建的区间的右端点
        """
        if l == r:  #* 如果左右端点相等, 说明是叶子节点, 直接赋值即可
            #* 因为l的范围是[1, n], 所以作为数组的索引时需要减一
            self.mx[o] = self.nums[l-1]
            return
        
        #* 否则需要递归遍历左右子树
        mid = (l+r)//2
        self.build(o*2, l, mid)
        self.build(o*2+1, mid+1, r)
        self.mx[o] = max(self.mx[o*2], self.mx[o*2+1])
        
    #* 具体操作就是update[1, 1, n, idx, val], 前面三个参数是不变的
    def update(self, o: int, l: int, r: int, idx: int, val: int)->None:
        """将idx位置的值更新为val
        #! 需要注意的是idx的范围是[1, n]并不是从0开始

        Args:
            o (int): 当前的节点编号
            l (int): 当前的节点所对应的区间左端点
            r (int): 当前的节点所对应的区间右端点
            idx (int): 需要更新的位置
            val (int): 需要更新的值
        """
        if l == r:
            self.mx[o]=val
            return
        
        mid = (l+r)//2
        #* 需要判断idx在左右哪个区间内
        if(idx <= mid):
            self.update(o*2, l, mid, idx, val)
        else:
            self.update(o*2+1, mid+1, r, idx, val)
        self.mx[o] = max(self.mx[o*2], self.mx[o*2+1])
    
    
    #* 具体操作就是query_max[1, 1, n, L ,R], 前面三个参数是不变的
    def query_max(self, o: int, l: int ,r: int, L: int, R: int)->int:
        """求[L, R]的最大值

        Args:
            o (int): 当前的节点编号
            l (int): 当前节点所对应的区间的左端点
            r (int): 当前节点所对应的区间的右端点
            L (int): 查询的区间的左端点
            R (int): 查询的区间的右端点

        Returns:
            int: 区间最大值
        """
        if L<=l and R>=r:
            return self.mx[o]

        mx = -inf
        mid = (l+r)//2
        if(L <= mid):
            mx = max(mx, self.query_max(o*2, l, mid, L, R))
        if(R > mid):
            mx = max(mx, self.query_max(o*2+1, mid+1, r, L, R))
        return mx

class SegmentTreeRangeModifyAdd:
    """线段树区间修改, 区间求和, 可以用树状数组平替
    需要用到lazy tag
    lazy tag: 用一个数组维护每个区间需要更新的值
    如果这个值 = 0, 表示不需要更新
    如果这个值 != 0, 表示更新操作在这个区间停住了, 不继续递归更新子区间了
    如果后面又来了一个更新破坏了lazy tag的区间, 那就得继续更新
    #! 当添加懒标记的时候对当前区间进行更新, 但是不对子区间进行更新
    #! 不一定用0来做判断, 但是对于求和来说是0
    
    """
    def __init__(self, n: int, nums: List[int]) -> None:
        """初始化线段树类

        Args:
            n (int): 初始数组的长度
            nums (List[int]): 初始的数组
        """
        self.sm = [0] * (n*4)
        self.nums = nums
        self.build(1, 1, n)
        self.todo = [0] * (n*4) #! 存储区间更新是否停住了, 其他情况不一定是1(比如如果是区间乘, 就应该设置成1)
        
    def maintain(self, o: int)->None:
        """更新完左右子树后对当前节点进行维护

        Args:
            o (int): 当前的节点编号
        """
        self.sm[o] = self.sm[o*2] + self.sm[o*2+1]
        
    def build(self, o: int, l: int, r: int)->None:
        """构建[l, r]内的线段树

        Args:
            o (int): 当前的节点编号
            l (int): 要构建的区间的左端点
            r (int): 要构建的区间的右端点
        """
        if l == r:  #* 如果左右端点相等, 说明是叶子节点, 直接赋值即可
            #* 因为l的范围是[1, n], 所以作为数组的索引时需要减一
            self.sm[o] = self.nums[l-1]
            return
        
        #* 否则需要递归遍历左右子树
        mid = (l+r)//2
        self.build(o*2, l, mid)
        self.build(o*2+1, mid+1, r)
        self.maintain(o)
        
    #* 具体操作就是add[1, 1, n, L, R, add], 前面三个参数是不变的
    def update(self, o: int, l: int, r: int, L: int, R: int, add: int)->None:
        """在[L, R]区间都加上add
        #! 需要注意的是idx的范围是[1, n]并不是从0开始

        Args:
            o (int): 当前的节点编号
            l (int): 当前的节点所对应的区间左端点
            r (int): 当前的节点所对应的区间右端点
            L (int): 需要增加的区间的左端点
            R (int): 需要增加的区间的右端点
            add (int): 需要增加的数
        """
        if L <= l and r <= R:
            self.todo[o] += add  #* 不再继续递归更新了
            self.sm[o] += (r-l+1)*add
            return
        
        mid = (l+r)//2
        
        self.do(o, l, r)
        if mid>=L: self.update(o*2, l, mid, L, R, add)
        if mid < R: self.update(o*2+1, mid+1, r, L, R, add)
        self.maintain(o)
        
    def do(self, o: int, l: int, r: int):
        """将值传给子节点
        #! 其他的代码需要更新这个

        Args:
            o (int): 子节点的编号
            l (int): 当前节点所代表的区间的左端点
            r (int): 当前节点所代表的区间的右端点
        """
        mid = (l+r)//2
        if l!=r and self.todo[o] != 0:  #* 如果不是叶子节点并且有懒标记 
            #* 传给左右儿子
            self.todo[o*2] += self.todo[o]
            self.todo[o*2+1] += self.todo[o]
            self.sm[o*2] += (mid-l+1) * self.todo[o]
            self.sm[o*2+1] += (r-mid) * self.todo[o]
            #* 自身清空
            self.todo[o] = 0
    
    #* 具体操作就是query_sum[1, 1, n, L ,R], 前面三个参数是不变的
    def query_sum(self, o: int, l: int ,r: int, L: int, R: int)->int:
        """求[L, R]的区间和

        Args:
            o (int): 当前的节点编号
            l (int): 当前节点所对应的区间的左端点
            r (int): 当前节点所对应的区间的右端点
            L (int): 查询的区间的左端点
            R (int): 查询的区间的右端点

        Returns:
            int: 区间和
        """
        if L<=l and R>=r:
            return self.sm[o]

        sm = 0
        self.do(o, l, r)
        mid = (l+r)//2
        if(L <= mid):
            sm += self.query_sum(o*2, l, mid, L, R)
        if(R > mid):
            sm += self.query_sum(o*2+1, mid+1, r, L, R)
        return sm
