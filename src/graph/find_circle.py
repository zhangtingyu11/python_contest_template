"""
在图中判断环是否存在
分为有向图找环 和 无向图找环
如果是有向图, 需要用dfs, 判断下一个要访问的节点在不在系统栈中
如果是无向图, 只需要判断访问的节点有没有被访问过即可
"""

from typing import List
def direct_have_circle(g: List[List[int]]) -> bool:
    """
    g为临界表, 点的编号为0 ~ len(g)-1
    """
    n = len(g)
    #* 该节点在不在系统栈中
    inStack = [False] * n
    vis = [False] * n
    ans = False
    def dfs(root):
        inStack[root] = True
        if vis[root]:return
        vis[root] = True
        nonlocal ans
        for node in g[root]:
            if inStack[node]:
                ans = True
                return 
            if not vis[node]:
                dfs(node)
        inStack[root] = False
    for root in range(n):
        if not vis[root]:
            dfs(root)
    return ans

def undirect_have_circle(g: List[List[int]]) -> bool:
    """
    g为临界表, 点的编号为0 ~ len(g)-1
    """
    n = len(g)
    #* 该节点在不在系统栈中
    vis = [False] * n
    ans = False
    def dfs(root):
        if vis[root]:return
        vis[root] = True
        nonlocal ans
        for node in g[root]:
            if not vis[node]:
                dfs(node)
            else:
                nonlocal ans
                ans = True
                return 
    for root in range(n):
        if not vis[root]:
            dfs(root)
    return ans
        