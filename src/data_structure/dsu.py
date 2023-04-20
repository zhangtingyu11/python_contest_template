"""
并查集是一种用于管理元素所属集合的数据结构，实现为一个森林，其中每棵树表示一个集合，树中的节点表示对应集合中的元素。

顾名思义，并查集支持两种操作：

合并(Union): 合并两个元素所属集合(合并对应的树)
查询(Find): 查询某个元素所属集合(查询对应的树的根节点), 这可以用于判断两个元素是否属于同一集合
"""

class Dsu():
    def __init__(self, size: int) -> None:
        """初始情况下所有的节点的父亲都是自己本身

        Args:
            size (int): 节点的个数
        """
        self.pa = list(range(size))
        
    
    def find(self, x: int)->int:
        """找到当前节点的最上层父节点

        Args:
            x (int): 当前节点

        Returns:
            int: 最上层父节点
        """
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    
    def union(self, x: int, y:int)->None:
        """将x合并到y上

        Args:
            x (int): 需要合并的节点1
            y (int): 需要合并的节点2
        """
        self.pa[self.find(x)] = self.find(y)