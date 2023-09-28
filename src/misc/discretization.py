"""
离散化
场景就是我可能只需要处理边界的情况而不用考虑中间的情况, 那么可以用离散化
一维的情况: 
    比如有一个数轴, 有m个区间, 区间上每个整数点都有一个点, 问点数最多的位置有多少个点
    如果值域特别大, 需要进行离散化
    比如[1,3], [2,4], [3, 6]
    我们离散化需要先对数组去重排序[1, 2, 3, 4, 6]
    这样的话1->0, 2->1, 3->2, 4->3, 6->5
    我们就得到了一个大值域往小值域的映射关系, 具体的可以是用二分查找找到映射的值
    
二维的情况:
    比如有个二维空间, 有m个矩形, 矩形范围内每个整数点都有一个点, 问点数最多的位置有多少个点
    相比于一维, 我们需要对x, y都进行离散化
"""

from typing import *
from bisect import *

def calculate_max_cnt_dim1(field: List[List[int]])->int:
    """给定多个区间[li, ri], [li, ri]区间内的整数位置都有一个点, 问点最多的位置有多少个点

    Args:
        field (List[List[int]]): 长度为m, 每个元素是[l, r], 表示[l, r]区间内的整数点都有一个点

    Returns:
        int: 点最多的位置的点的个数
    """
    #* 离散化
    diff = Counter()
    for start, end in field:
        diff[start] += 1
        diff[end + 1] -= 1
    s = sorted(diff.keys())
    pre = list(accumulate([diff[i] for i in s]))
    #* 其中pre[i]表示在[s[i], s[i+1])这个区间内有多少个点
    return max(pre)

from itertools import accumulate
def calculate_region_point_num_dim1(field: List[List[int]]):
    """给定多个区间[li, ri], [li, ri]区间内的整数位置都有一个点, 求每个区间有多少个点

    Args:
        field (List[List[int]]): 长度为m, 每个元素是[l, r], 表示[l, r]区间内的整数点都有一个点

    Returns:
        int: 每个区间的点个数
    """
    diff = Counter()
    for start, end in field:
        diff[start] += 1
        diff[end + 1] -= 1
    s = sorted(diff.keys())
    pre = list(accumulate([diff[i] for i in s]))
    #* 其中pre[i]表示在[s[i], s[i+1])这个区间内有多少个点
    return pre


def calculate_max_cnt_dim2(field: List[List[int]])->int:
    """给定多个区间[r1, c1, r2, c2], [r1, c1]为矩形左上角点的坐标, [r2, c2]为矩形右下角点的坐标, 
       矩形内每个整数点都有一个点, 问点最多的位置有多少个点

    Args:
        field (List[List[int]]): 长度为m, 每个元素是[r1, c1, r2, c2]

    Returns:
        int: 点最多的位置的点的个数
    """
    
    xs, ys = set(), set()
    for r1, c1, r2, c2 in field:
        xs.add(r1)
        xs.add(r2)
        ys.add(c1)
        ys.add(c2)
    xs = sorted(xs)
    ys = sorted(ys)
    
    #* 离散化后总共有n个数
    m, n = len(xs), len(ys)
    #* 创建差分数组
    diff = [[0] * (n+2) for _ in range(m+2)]
    for r1, c1, r2, c2 in field:
        x1 = bisect_left(xs, r1)
        x2 = bisect_left(xs, r2)
        y1 = bisect_left(ys, c1)
        y2 = bisect_left(ys, c2)
        diff[x1+1][y1+1]+=1
        diff[x1+1][y2+2]-=1
        diff[x2+2][y1+1]-=1
        diff[x2+2][y2+2]+=1
    
    ans = 0
    #* 用diff来存储前缀和
    for i in range(1, m+1):
        for j in range(1, n+1):
            diff[i][j]+=diff[i-1][j]+diff[i][j-1]-diff[i-1][j-1]
            if(diff[i][j] > ans):
                ans = diff[i][j]
    return ans
    