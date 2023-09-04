"""
二叉搜索树
! 定义
二叉搜索树是一种二叉树的树形数据结构，其定义如下：
1. 空树是二叉搜索树。
2. 若二叉搜索树的左子树不为空, 则其左子树上所有点的附加权值均小于其根节点的值。
3. 若二叉搜索树的右子树不为空, 则其右子树上所有点的附加权值均大于其根节点的值。
4. 二叉搜索树的左右子树均为二叉搜索树。
"""

"""
! 性质
二叉搜索树的中序遍历结果是非递减
"""


"""
给定二叉搜索树的后序遍历/前序遍历结果还原二叉搜索树
"""
from python_contest_template.binary_tree import TreeNode
from math import inf
from collections import *
def restore_post(s: str):
    """利用后序遍历的结果还原二叉搜索树

    Args:
        s (str): 二叉搜索树的后序遍历结果, 用' '分隔

    Returns:
        _type_: 返回二叉搜索树的根节点
    """
    arr = list(map(int, s.split()))
    def construct(lower: int, upper: int) -> TreeNode:
        #* 当出现以下情况说明子树遍历完了
        if arr == [] or arr[-1] < lower or arr[-1] > upper:
            return None
        #* 因为是后序遍历, 所以数组的前半部分是左子树, 后半部分是右子树, 那么最靠后的部分就是右节点
        #* 当比根节点大的部分都遍历完的时候就是下一个就是左节点
        val = arr.pop()
        root = TreeNode(val)
        root.right = construct(val, upper)
        root.left = construct(lower, val)
        return root
    return construct(-inf, inf)

def restore_pre(s: str):
    """利用前序遍历的结果还原二叉搜索树

    Args:
        s (str): 二叉搜索树的前序遍历结果, 用' '分隔

    Returns:
        _type_: 返回二叉搜索树的根节点
    """
    arr = deque(map(int, s.split()))
    def construct(lower: int, upper: int) -> TreeNode:
        #* 当出现以下情况说明子树遍历完了
        if arr == deque() or arr[0] < lower or arr[0] > upper:
            return None
        #* 因为是前序遍历, 所以数组的前半部分是左子树, 后半部分是右子树, 那么最靠前的部分就是左节点
        #* 当比根节点小的部分都遍历完的时候就是下一个就是右节点
        val = arr.popleft()
        root = TreeNode(val)
        root.left = construct(lower, val)
        root.right = construct(val, upper)
        return root
    return construct(-inf, inf)

    

