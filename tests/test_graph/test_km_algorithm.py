"""
使用KM算法可以在O(n**4)时间内求出二分图的最大权完美匹配
首先需要一个n*n的矩阵, 记录左右两个顶点存在的边的权重, 如果不存在边则记为0
令S为二分图左边匹配的点, T为二分图右边匹配的点, S'为二分图左边未匹配的点, T'为二分图右边未匹配的点
需要给所有的点设置一个顶标, 初始情况下, 左边的点的顶标为和他相连的边的最大权重, 右边的点的顶标均为0
lx表示左边的点的顶标, ly表示右边的点的顶标, w[u][v]表示u, v顶点连线的权重
加边需要满足lx[u] + ly[v] == w[u][v]
如果加到一条边无论如何都加不下去了, 就需要在S和T'中找到所有的配对, 求出a = {min(lx[u] + ly[v] - w[u][v]) | u \in S, v \in T'}
然后让S中的所有顶标-a, T中的所有顶标+a

参考OJ的题目https://uoj.ac/problem/80
"""
from math import inf
class Hungarian:
    def __init__(self, n, m):
        """初始化函数

        Args:
            n (_type_): 左边点的个数
            m (_type_): 右边点的个数
        """
        n = max(n, m)   #* 取较大值构建方阵
        self.n = n
        self.g = [[0] * n for _ in range(n)]    #* 权重图
        self.match = [-1] * n   #* 右点匹配的左点
        
    def addEdge(self, u, v, w) :
        self.g[u][v] = max(w, 0)
        
    def dfs(self, x):
        self.visx[x] = True
        n = self.n
        for y in range(n):  #* 遍历所有的右点
            if not self.visy[y]:
                delta = self.lx[x] + self.ly[y] - self.g[x][y]
                if delta == 0:
                    self.visy[y] = True
                    if self.match[y]==-1 or self.dfs(self.match[y]):    #* 如果这个右点没匹配, 或者匹配的左点可以匹配别的值
                        self.match[y] = x
                        return True
                else:
                    self.slack[y] = min(self.slack[y], delta)    #* 更新slack
        return False
                
    def solve(self):
        n = self.n
        self.lx = [-inf] * n
        #* 初始化lx, ly
        for i in range(n):
            for j in range(n):
                self.lx[i] = max(self.lx[i], self.g[i][j])
        self.ly = [0] * n
        
        for i in range(n):  #* 遍历所有的左节点
            """
            初始化vis数组, slack数组
            """
            while(True):
                self.visx = [False] * n
                self.visy = [False] * n
                self.slack = [inf] * n
                if self.dfs(i): break
                
                #* 说明找不到匹配点, 要更新顶标
                a = inf
                for j in range(n):
                    if not self.visy[j]:
                        a = min(self.slack[j], a)
                for j in range(n):
                    if self.visx[j]: self.lx[j]-=a
                    if self.visy[j]: self.ly[j]+=a
        
        res = 0
        for i in range(n):
            res += self.g[self.match[i]][i]
        return res
                        
import sys
input = lambda: sys.stdin.readline().strip()

nl, nr, m = list(map(int, input().split()))
hug = Hungarian(nr, nl)
for i in range(m):
    u, v, w = list(map(int, input().split()))
    v-=1
    u-=1
    hug.addEdge(u, v, w)
    
res = hug.solve()
ans = [0] * nl
for i in range(nr):
    m = hug.match[i]
    if m == -1 or hug.g[m][i] == 0:
        pass
    else:
        ans[m] = i+1
print(res)
print(*ans, sep = ' ')

"""
2 2 3
1 1 100
1 2 1
2 1 1

10 20 15
6 13 192308866
8 19 566615502
4 6 431289733
9 9 636005760
10 20 227361595
8 5 411186020
9 7 980308961
8 4 176912056
5 5 857519265
2 10 863033384
6 12 39871653
3 4 5431932
6 5 813069917
3 3 625301887
1 11 598372108

5342111301
11 10 3 6 5 13 0 19 7 20 

5149802435
11 10 3 6 5 0 0 19 7 20
"""
    
    

        
            
            
        
                            
                
        
        
