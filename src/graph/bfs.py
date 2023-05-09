"""
广度优先搜索(BFS)
可以用来遍历图, 或者求图中两点的最短距离
"""
from typing import List
from collections import *
from heapq import *

def bfs_use_deque(graph: List[List[int]], start: int) -> int:
    """给定一个连通图, 遍历这个图, 返回从起点开始的最长路径
    使用双端队列实现

    Args:
        graph (List[List[int]]): 列表中第i个元素存储节点i的邻接点
        start (int): 遍历的起始节点
    Return: 最长路径值
    """
    vis = set()
    q = deque()
    q.append(start)
    vis.add(start)
    level = 0
    while(q):
        for _ in range(len(q)):
            cur = q.popleft()
            for node in graph[cur]:
                if(node not in vis):
                    q.append(node)
                    vis.add(node)
        level+=1
    return level-1
    
def bfs_use_two_array(graph: List[List[int]], start: int) -> int:
    """给定一个连通图, 遍历这个图, 返回从起点开始的最长路径
    使用双数组实现

    Args:
        graph (List[List[int]]): 列表中第i个元素存储节点i的邻接点
        start (int): 遍历的起始节点
    Return: 最长路径值
    """
    vis = set()
    q = []
    q.append(start)
    vis.add(start)
    level = 0
    while(q):
        nq = []
        for cur in q:
            for node in graph[cur]:
                if(node not in vis):
                    nq.append(node)
                    vis.add(node)
        q = nq
        level+=1
    return level-1

def bfs_use_heap(graph: List[List[int]], start: int, end: int)->int:
    """堆优化的bfs, 返回从start出发到终点的最短路径
    一般是处理最短xxx的问题, 并且不能通过普通bfs解决
    这时候需要将(要求的最短的值的当前值, 位置) push 到优先队列中
    这样pop的时候会将最小的值pop出来
    
    Args:
        graph (List[List[int]]): 列表中第i个元素存储节点i的邻接点
        start (int): 遍历的起始节点
        end (int): 需要到达的终点节点

    """
    vis = set()
    pq = []
    heappush(pq, (0, start))
    vis.add(start)
    while(pq):
        level, cur = heappop(pq)
        if(cur == end): return level
        for node in graph[cur]:
            if(node not in vis):
                heappush(pq, (level+1, node))
                vis.add(node)
            
            
    
    
    
    
