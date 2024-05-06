"""
使用KM算法可以在O(n**4)时间内求出二分图的最大权完美匹配, DFS是4次方, BFS是3次方
首先需要一个n*n的矩阵, 记录左右两个顶点存在的边的权重, 如果不存在边则记为0
令S为二分图左边匹配的点, T为二分图右边匹配的点, S'为二分图左边未匹配的点, T'为二分图右边未匹配的点
需要给所有的点设置一个顶标, 初始情况下, 左边的点的顶标为和他相连的边的最大权重, 右边的点的顶标均为0
lx表示左边的点的顶标, ly表示右边的点的顶标, w[u][v]表示u, v顶点连线的权重
加边需要满足lx[u] + ly[v] == w[u][v]
如果加到一条边无论如何都加不下去了, 就需要在S和T'中找到所有的配对, 求出a = {min(lx[u] + ly[v] - w[u][v]) | u \in S, v \in T'}
然后让S中的所有顶标-a, T中的所有顶标+a

下面的代码实现是从左边点找右边点
左边到右边一定是匹配边, 右边到左边一定是非匹配边
"""
from math import inf
class Hungarian:
    def __init__(self, n, m):
        """初始化函数

        Args:
            n (_type_): 左边点的个数
            m (_type_): 右边点的个数
        """
        n = max(n, m)   #* 以较多的点数构造方阵
        self.n = n
        self.g = [[0] * self.n for _ in range(self.n)]        #* 构造一个n*n的方阵
        self.match = [-1] * n   #* 左点对应的匹配点
        
    def addEdge(self, u, v, w) :
        """
        在左点u和右点v直接加一条权重为w的边
        可以使用
        """
        self.g[u][v] = max(w, 0)    #* 如果是负数, 还不如不加
        
    def dfs(self, x):
        self.visx[x] = True
        for y in range(self.n): #* 遍历所有的右节点
            if not self.visy[y]:    #* 需要右节点没有被访问过, 也就是没有匹配过
                delta = self.lx[x] + self.ly[y] - self.g[x][y]
                if delta == 0:  #* 这种情况下是可以匹配的
                    self.visy[y] = True
                    if self.match[y]==-1 or self.dfs(self.match[y]):    #* 如果右节点没有被匹配过或者它的左节点可以选别的
                        self.match[y] = x   #* 匹配两个节点
                        return True
                else:   #* 这种情况y在T'中, 需要更新slack
                    self.slack[y] = min(self.slack[y], delta)
        return False

    def solve(self):
        #* 初始化
        n = self.n
        self.lx = [-inf] * n     #* 左点的顶标
        for i in range(n):
            for j in range(n):
                self.lx[i] = max(self.lx[i], self.g[i][j])
        self.ly = [0] * n    #* 右点的顶标
        
        for i in range(n): #* 遍历所有的左节点
            while(True):
                self.visx = [False] * n
                self.visy = [False] * n
                self.slack = [inf] * n
                if self.dfs(i):break
                
                #* 说明不行
                a = inf
                #* 计算a
                for j in range(n):
                    if not self.visy[j]:
                        a = min(a, self.slack[j])
                for j in range(n):
                    if self.visx[j]: self.lx[j] -= a
                    if self.visy[j]: self.ly[j] += a
        res = 0
        for i in range(n):
            res += self.g[self.match[i]][i]
        return res
                        
                    

    

        
            
            
        
                            
                
        
        
