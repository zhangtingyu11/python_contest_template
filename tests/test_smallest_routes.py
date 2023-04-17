from graph.smallest_routes import *
import unittest

class Test_TestCommonDijkstra(unittest.TestCase):
    def convert_edges_to_graph(self, n: int, edges:List[List[int]])->List[List[List[int]]]:
        """将边转化为图

        Args:
            n (int): 总节点的个数, 节点标号范围为[0, n-1]
            edges (List[List[int]]): 边, 每个元素是一个列表, 存储三个值, [x, y, w], x表示起点, y表示终点, w表示xy这条边的权重

        Returns:
            List[List[List[int]]]: 返回图, g[x]存放列表, 列表中每个元素是一个二元列表[y, w], 表示他的连接点和xy之间的权重
        """

        g = [[] for _ in range(n)]
        for x, y ,w in edges:
            g[x].append([y, w])
        return g
    
    def test_common_dijkstra0(self):
        edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
        n = 4
        start = 0
        ans = [0, 2, 3, inf]
        graph = self.convert_edges_to_graph(n, edges)
        self.assertEqual(common_dijkstra(graph, start), ans)
        
        
class Test_TestFloyd(unittest.TestCase):
    def convert_edges_to_graph(self, n, edges):
        g = [[inf] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, w in edges:
            g[x][y] = w
        return g 

    def test_floyd(self):
        edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
        n = 4
        ans = [[0, 2, 3, inf],
               [inf, 0, 1, inf],
               [inf, inf, 0, inf],
               [3, 5, 6, 0]]
        graph = self.convert_edges_to_graph(n, edges)
        self.assertEqual(floyd(graph), ans)
        
        
class Test_TestHeapDijkstra(unittest.TestCase):
    def convert_edges_to_graph(self, n: int, edges:List[List[int]])->List[List[List[int]]]:
        """将边转化为图

        Args:
            n (int): 总节点的个数, 节点标号范围为[0, n-1]
            edges (List[List[int]]): 边, 每个元素是一个列表, 存储三个值, [x, y, w], x表示起点, y表示终点, w表示xy这条边的权重

        Returns:
            List[List[List[int]]]: 返回图, g[x]存放列表, 列表中每个元素是一个二元列表[y, w], 表示他的连接点和xy之间的权重
        """

        g = [[] for _ in range(n)]
        for x, y ,w in edges:
            g[x].append([y, w])
        return g
    
    def test_common_dijkstra0(self):
        edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
        n = 4
        start = 0
        ans = [0, 2, 3, inf]
        graph = self.convert_edges_to_graph(n, edges)
        self.assertEqual(heap_dijkstra(graph, start), ans)


    
    