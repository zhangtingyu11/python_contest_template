"""
#! 二分查找

#TODO 还有bisect_right的模板
"""
from typing import List
from bisect import *

def find_bigger_and_equal(nums: List[int], target: int)->int:
    """求第一个大于等等于target值的索引
    如果结果为len(nums), 则表示没有大于等于target的数

    Args:
        nums (List[int]): 已经从小到大排序好的数组
        target (int): 需要大于等于的目标值

    Returns:
        int: 返回索引值
    """
    return bisect_left(nums, target)

def find_bigger(nums: List[int], target: int)->int:
    """找到第一个大于target值的索引
    如果结果为len(nums), 则表示没有大于target的数

    Args:
        nums (List[int]): 已经从小到大排序好的数组              
        target (int): 需要大于的目标值

    Returns:
        int: 返回索引值
    """
    return bisect_left(nums,target+1)

def find_smaller_and_equal(nums: List[int], target: int)->int:
    """找到最后一个小于等于target值的索引
    如果结果为-1, 则表示没有小于等于target的值

    Args:
        nums (List[int]): 已经从小到大排序好的数组
        target (int): 需要小于等于的目标值

    Returns:
        int: 返回索引值
    """
    return bisect_left(nums, target+1)-1

def find_smaller(nums: List[int], target: int)->int:
    """找到最后一个小于target值的索引
    如果结果为-1, 则表示没有小于target的值

    Args:
        nums (List[int]): 已经从小到大排序好的数组
        target (int): 需要小于的值

    Returns:
        int: 返回索引值
    """
    return bisect_left(nums, target)-1


def judge_in_range(nums: List[int], left, right)->bool:
    """判断有序nums中有没有在[left, right]区间内的数

    Args:
        nums (List[int]): 有序的数组
        left (_type_): 区间的左端点
        right (_type_): 区间的右端点

    Returns:
        bool: 存在返回True, 否则返回False
    """
    bidx1 = bisect_left(nums, left)
    bidx2 = bisect_right(nums, right)
    if bidx1 == bidx2:
        return False
    return True