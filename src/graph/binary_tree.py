"""
二叉树
! 定义
每个结点最多只有两个儿子（子结点）的有根树称为二叉树。常常对两个子结点的顺序加以区分，分别称之为左子结点和右子结点。
大多数情况下，二叉树一词均指有根二叉树。
"""

"""
! 性质
1.二叉树的中序遍历和任意一个其他的遍历(前序遍历和后序遍历)都可以唯一确定一棵树
  前序的第一个是root, 后序的最后一个是root。
  先确定根节点，然后根据中序遍历, 在根左边的为左子树, 根右边的为右子树。
  对于每一个子树可以看成一个全新的树, 仍然遵循上面的规律。
"""

