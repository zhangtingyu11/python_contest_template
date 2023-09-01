"""
最小生成树
定义无向连通图的 最小生成树(Minimum Spanning Tree, MST)为边权和最小的生成树。
"""

"""
Kruskal 算法
这是一种贪心算法, 简单来说, 就是对所有的边按照边权就行排序
初始情况下, 所有的边都属于自己这一棵树, 如果遍历到的一条边属于不同的树就可以将他们合并, 可以使用并查集来维护边的两个节点是否属于同一棵树

下面以二维节点举例, 以两个节点的曼哈顿举例来表示连接两个节点的边的权重大小
"""
from typing import List

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
    
    
    def union(self, x: int, y:int)->bool:
        """将x合并到y上

        Args:
            x (int): 需要合并的节点1
            y (int): 需要合并的节点2
        """
        px, py = self.find(x), self.find(y)
        if(px == py):
            return False
        
        self.pa[px] = py
        return True

def kruskal(points: List[List[int]]):
    def dist(point1, point2):
        return abs(point1[0]-point2[0]) + abs(point1[1] - point2[1])
    
    dis = list()
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            dis.append((dist(points[i], points[j]), i, j))
            
    dis.sort()
    dsu = Dsu(n)
    ans, num = 0, 1
    for d, x, y in dis:
        if(dsu.union(x, y)):
            num+=1        
            ans+=d
            if(num == n):
                break
    return ans
    