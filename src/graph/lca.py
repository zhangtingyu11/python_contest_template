"""
最近公共祖先
求树上两个节点的最近公共祖先
"""

"""
利用倍增求最近公共祖先
设节点i的深度为 depth[i]。这可以通过一次 DFS 预处理出来。

假设 depth[x]≤depth[y]（否则交换两点）。我们可以先把更靠下的 y 更新为 y 的第 depth[y]-depth[x]个祖先节点，这样 x 和 y 就处在同一深度了。

如果此时 x=y, 那么 x 就是 lca。否则说明 lca\在更上面，那么就把 x 和 y 一起往上跳。

由于不知道 lca 的具体位置，只能不断尝试，先尝试大步跳，再尝试小步跳。设 i=⌊log2n⌋, 循环直到 i<0。每次循环:

如果 x 的第 2^i个祖先节点不存在, 即 pa[x][i]=-1, 说明步子迈大了，将 i 减 1, 继续循环。
如果 x 的第 2^i个祖先节点存在, 且 pa[x][i]≠pa[y][i], 说明 lca在 pa[x][i]的上面，那么更新 x 为 pa[x][i],
更新 y 为 pa[y][i]，将 i 减 1, 继续循环。否则，若 pa[x][i]=pa[y][i]，那么 lca可能在 pa[x][i]下面，由于无法向下跳，只能将 i 减 1, 继续循环。
上述做法能跳就尽量跳,不会错过任何可以上跳的机会。所以循环结束时,x 与 lca只有一步之遥, 即 lca=pa[x][0]。
"""
from typing import List
class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return self.pa[x][0]
