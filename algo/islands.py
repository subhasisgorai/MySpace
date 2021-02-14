from collections import namedtuple
from pprint import pprint
from algo.union_find import Partition

Node = namedtuple('Node', ('x', 'y'))


class GridAsGraph:

    def __init__(self, grid):
        if grid:
            self.all_nodes = list()
            m = len(grid)
            n = len(grid[0])
            for x in range(m):
                for y in range(n):
                    if matrix[x][y] == 1:
                        self.all_nodes.append(Node(x , y))

    def neighbors(self, current_node):
        return [node for node in 
                    map(Node, (current_node.x - 1, current_node.x + 1, current_node.x, current_node.x),
                        (current_node.y, current_node.y, current_node.y - 1, current_node.y + 1)) 
                    if node in self.all_nodes]
        
    def merge_neighbors(self):
        p = Partition()
        positions = dict()
        
        for node in self.all_nodes:
            positions[node] = p.make_group(node)
            
        for node in self.all_nodes:
            for neighbor in self.neighbors(node):
                a = p.find(positions[node])
                b = p.find(positions[neighbor])
                
                if a != b:
                    p.union(a, b)
        
        return p
    
    def count_islands(self):
        return len(self.merge_neighbors())    


if __name__ == '__main__':
    matrix = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
    pprint(matrix, width=32)
    graph = GridAsGraph(matrix)
    print 'Number of islands: {}'.format(graph.count_islands())
