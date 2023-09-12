"""
拓扑排序
拓扑排序的目标是将所有节点排序，使得排在前面的节点不能依赖于排在后面的节点。

可以处理图中两两元素之间的依赖关系
"""
from typing import List
from collections import defaultdict, deque

def topological_sorting(n, edges: List[List[int]])->List[int]:
    """拓扑排序

    Args:
        n (_type_): 节点个数
        edges (List[List[int]]): 边, 每个元素[x, y]对应x->y

    Returns:
        List[int]: 一种可行的拓扑排序的结果
    """
    #* 建图
    g = defaultdict(list)
    #* 计算每个点的入度
    degrees = [0] * n
    for x, y in edges:
        degrees[y]+=1
        g[x].append(y)
        
    q = deque()
    #* 找到入度为0的点加入队列中
    for idx, d in enumerate(degrees):
        if d==0:
            q.append(idx)
    
    ans = []   
    while(q):
        for _ in range(len(q)):
            cur = q.popleft()
            ans.append(cur)
            for node in g[cur]:
                degrees[node]-=1
                #* 如果这个点入度为0了加入队列中
                if(degrees[node]==0):
                    q.append(node)
    return ans
            
    