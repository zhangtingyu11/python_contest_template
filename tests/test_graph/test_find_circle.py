from graph.find_circle import *
import unittest

class Test_TestDirectFindCircle(unittest.TestCase):
    def convert_edges_to_graph(self, n: int, edges:List[List[int]])->List[List[List[int]]]:
        """将边转化为图

        Args:
            n (int): 总节点的个数, 节点标号范围为[0, n-1]
            edges (List[List[int]]): 边, 每个元素是一个列表, 存储三个值, [x, y], x表示起点, y表示终点

        Returns:
            List[List[List[int]]]: 返回图, g[x]存放列表, 列表中每个元素是它指向的点
        """

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
        return g
    
    def test_direct_have_circle0(self):
        edges = [[0, 0], [0, 1], [1, 2]]
        n = 3
        graph = self.convert_edges_to_graph(n, edges)
        self.assertTrue(direct_have_circle(graph))
        
    def test_direct_have_circle1(self):
        edges = [[0, 3], [0, 1], [1, 2]]
        n = 4
        graph = self.convert_edges_to_graph(n, edges)
        self.assertFalse(direct_have_circle(graph))
        

class Test_TestUndirectFindCircle(unittest.TestCase):
    def convert_edges_to_graph(self, n: int, edges:List[List[int]])->List[List[List[int]]]:
        """将边转化为图

        Args:
            n (int): 总节点的个数, 节点标号范围为[0, n-1]
            edges (List[List[int]]): 边, 每个元素是一个列表, 存储三个值, [x, y], x表示起点, y表示终点

        Returns:
            List[List[List[int]]]: 返回图, g[x]存放列表, 列表中每个元素是它指向的点
        """

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
        return g
    
    def test_undirect_have_circle0(self):
        edges = [[0, 0], [0, 1], [1, 2]]
        n = 3
        graph = self.convert_edges_to_graph(n, edges)
        self.assertTrue(undirect_have_circle(graph))
        
    def test_undirect_have_circle1(self):
        edges = [[0, 2], [0, 1], [1, 2]]
        n = 4
        graph = self.convert_edges_to_graph(n, edges)
        self.assertTrue(undirect_have_circle(graph))