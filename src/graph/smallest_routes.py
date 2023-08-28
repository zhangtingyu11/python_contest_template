from typing import List
from math import *
from heapq import *

"""
! Floyd算法:
! 优点: 可以在O(n^3)情况下算出两两之间的最短路径, 适用于计算两两点的最短路径, 可以处理负权
"""
def floyd(g: List[List[int]])->List[List[int]]:
    """Floyd算法
        本质上是一个动态规划, 记g[k][x][y]为除了x,y外, 节点的最大标号为k的最短路径长度
        那么g[k][x][y] = min(g[k-1][x][y], g[k-1][x][k]+g[k-1][k][y])
        然后压缩第一维:
            g[x][y] = min(g[x][y], g[x][k]+g[k][y])
        为什么可以压缩第一维？
        答:
        现在我们需要证明将 g[k][x][y] 直接在原地更改也不会更改它的结果：
        我们注意到 g[k][x][y] 的涵义是第一维为 k-1 这一行和这一列的所有元素的最小值，
        包含了 g[k-1][x][y]，那么我在原地进行更改也不会改变最小值的值，因为如果将该三维矩阵压缩为二维，
        则所求结果 g[x][y] 一开始即为原 g[k-1][x][y] 的值，最后依然会成为该行和该列的最小值。
    
    Args:
        g (List[List[int]]): 记录两点之间的直接距离值, g[x][x] = 0, 
                             如果两点直接不是直接相连, 那他们的距离是inf
                             注意, 节点为len(g)个, 且节点的标号范围为[0, len(g)-1]
    return: 
        List[List[int]]: 两两点之间的最短距离的矩阵
    """
    n = len(g)
    for k in range(n):
        for x in range(n):
            for y in range(n):
                g[x][y] = min(g[x][y], g[x][k] + g[k][y])
    return g
     
     
"""
#! Dijkstra算法
#! 优点: 可以不用计算两两点之间的最短路径, 可以求出某一起点开始的最短路径
#! 缺点: 不能处理负权
#! 时间复杂度: O(n^2), 如果求两两点之间的最短路, 也是O(n^3)
#! Dijkstra算法可以保证在跑一次算法中每个点只遇到一次, 也就是说从起点到已经遍历到的点的路径在后续更新最短路的过程中, 其最短路不会变化
"""
def common_dijkstra(g: List[List[List[int]]], start: int) -> List[int]:
    """dijkstra算法
    本质上是个贪心, 选择当前权值最小的路径

    Args:
        g (List[List[List[int]]]): 图, g[x]存储两个值(x, w)构成的列表, y表示相邻的节点, w表示x和y相连的这条边的权重
        start (int): 起点编号

    Returns:
        List[int]: 返回当前起点到其他节点的最短路径
    """
    n = len(g)
    dis = [inf] * n
    dis[start] = 0
    vis = [False]*n #* 标记已经被更新成最短路的点
    for i in range(n):
        x = -1
        for j in range(n):
            if(not vis[j] and (x<0 or dis[j] < dis[x])):   #* 如果没有被标记过且当前的最短路, 那么就用x来更新其他点
                x = j
        vis[x] = True
        for y, w in g[x]:
            if(dis[y] > dis[x] + w):
                dis[y] = dis[x] + w
    return dis


"""
#! 堆优化的Dijkstra算法
#! 时间复杂度O(mlogm), 在稀疏图中m = O(n), 此时堆优化的Dijkstra比朴素Dijkstra要好
#! 在稠密图中, m = O(n^2), 此时朴素Dijkstra更好
"""

def heap_dijkstra(g: List[List[List[int]]], start: int)->List[int]:
    """堆优化的dijkstra算法

    Args:
        g (List[List[List[int]]]): 图, g[x]存储两个值(x, w)构成的列表, y表示相邻的节点, w表示x和y相连的这条边的权重
        start (int): 起点编号

    Returns:
        List[int]: 返回当前起点到其他节点的最短路径
    """
    n = len(g)
    dis = [inf] * n
    dis[start] = 0
    q = [(0, start)]
    vis = set()
    while(q):
        _, x = heappop(q)
        if(x in vis): continue
        vis.add(x)
        for y, w in g[x]:
            if(dis[y] > dis[x]+w):
                dis[y] = dis[x]+w
                heappush(q, (dis[y], y))
    return dis
    



                
                
    
    
                

