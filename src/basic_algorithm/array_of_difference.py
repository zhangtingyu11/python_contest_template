from itertools import *
from typing import List
"""
!一维差分数组
可以当做是求和的逆运算
! 假设原数组是nums, 差分数组是diff, 数组长度为n, 则应该满足以下关系
if i == 0:
    diff[i] = nums[i]
else:
    diff[i] = nums[i]-nums[i-1]
    
! 差分数组满足以下几个性质
1. nums[i]的值是diff[i]的前缀和, nums[i] = sum(diff[j] for j in range(i+1))
2. 可以通过差分数组计算nums[i]的前缀和: pre_sum[n] = sum((n-j+1)*diff[j] for j in range(i, n))

! 差分数组可以用来处理在[l, r]区间内同时加上一个数k, 最后查询某个位置的数字的情况
diff[l]+=k
diff[r+1]-=k
"""

def calculate_diff(nums:List[int])->List[int]:
    """计算一阶差分数组

    Args:
        nums (List[int]): 长度为n的原始数组

    Returns:
        List[int]: 长度为n的差分数组
    """ 
    n = len(nums)
    diff = [nums[0]]
    for i in range(1, n):
        diff.append(nums[i]-nums[i-1])
    return diff

def calculate_origin_from_diff(diff:List[int])->List[int]:
    """从差分数组计算原始数组

    Args:
        diff (List[int]): 长度为n的差分数组

    Returns:
        List[int]: 长度为n的原始数组
    """
    nums = list(accumulate(diff))
    return nums

def calculate_pre_sum_from_diff(diff:List[int])->List[int]:
    """从差分数组中计算原始数组的前缀和

    Args:
        diff (List[int]): 长度为n的差分数组

    Returns:
        List[int]: 长度为n的原始数组的前缀和
    """
    pre_sum = [0] * len(diff)
    for i in range(len(diff)):
        pre_sum[i] = sum((i-j+1)*diff[j] for j in range(i+1))
    return pre_sum

def calculate_changed_nums(nums: List[int], changes:List[List[int]])->List[int]:
    """给定原始数组和数组变化的区间, 求变化后的数组

    Args:
        nums (List[int]): 长度为n的原始数组
        changes (List[List[int]]): 长度为m, 即原数组要变化m次, 每次变化是个长度为3的数组[start, end, k], 表示在[start, end]区间内的数都要增加k

    Returns:
        List[int]: 变化后的数组
    """
    diff = calculate_diff(nums)
    diff.append(0)
    for start, end, k in  changes:
        diff[start] += k
        diff[end+1]-=k
    pre_sum = list(accumulate(diff[:-1]))
    return pre_sum


"""
#! 二维差分数组
现在是对[row1, col1]到[row2, col2]的矩形范围内的数组都+k
从二维前缀和的角度来看对区域左上角+k 会对所有右下位置产生影响，那么在区域右上角的右边相邻处和左下角的下边相邻处
-k可以消除这个影响,s 但是两个-k又会对区域右下角的右下所有位置产生影响, 所以要在右下角的右下相邻处再+k还原回来。

#! 假设矩形的大小是m*n的, 一般我们将差分数组设置成(m+2)*(n+2)的, 去掉边缘宽度为1的m*n的矩形就是差分数据
#! 这么做是为了方便后面求二维前缀和
"""             

def calculate_changed_nums_dim2(grid: List[List[int]], changes:List[List[int]])->List[List[int]]:
    """给定原始grid, 和对应的区间变化changes, 求变化后的矩阵

    Args:
        grid (List[List[int]]): 原始的m*n的grid
        changes (List[List[int]]): 长度为N, 即变化N次, 每个变化为[r1, c1, r2, c2, k], 
                                   即左上角为[r1, c1], 右下角为[r2, c2]的矩形范围内的数都增加k

    Returns:
        List[List[int]]: 变化后的m*n的grid
    """
    m, n = len(grid), len(grid[0])
    #* 更新差分数组
    diff = [[0] * (n+2) for _ in range(m+2)]
    for r1, c1, r2, c2, k in changes:
        diff[r1+1][c1+1]+=k
        diff[r1+1][c2+2]-=k
        diff[r2+2][c1+1]-=k
        diff[r2+2][c2+2]+=k
    
    #* 计算二维前缀和
    for i in range(1, m+1):
        for j in range(1, n+1):
            diff[i][j] += diff[i-1][j]+diff[i][j-1]-diff[i-1][j-1]
            grid[i-1][j-1]+=diff[i][j]
    return grid
                

        

