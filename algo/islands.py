from collections import deque
from collections import namedtuple
from pprint import pprint

from algo.union_find import Partition

Node = namedtuple('Node', ('x', 'y'))


class GridAsGraph:
    __slots__ = '_all_nodes'

    def __init__(self, grid):
        if grid:
            self._all_nodes = list()
            m = len(grid)
            n = len(grid[0])
            for x in range(m):
                for y in range(n):
                    if matrix[x][y] == 1:
                        self._all_nodes.append(Node(x , y))

    def all_nodes(self):
        return tuple(self._all_nodes)
        
    def neighbors(self, current_node):
        return [node for node in 
                    map(Node, (current_node.x - 1, current_node.x + 1, current_node.x, current_node.x),
                        (current_node.y, current_node.y, current_node.y - 1, current_node.y + 1)) 
                    if node in self._all_nodes]
        
    def merge_neighbors(self):
        p = Partition()
        positions = dict()
        
        for node in self._all_nodes:
            positions[node] = p.make_group(node)
            
        for node in self._all_nodes:
            for neighbor in self.neighbors(node):
                a = p.find(positions[node])
                b = p.find(positions[neighbor])
                
                if a != b:
                    p.union(a, b)
        
        return p
    
    def count_islands(self):
        return len(self.merge_neighbors())
    

class Island:
    __slots__ = '_nodes', '_name' 
    
    def __init__(self, name):
        self._name = name
        self._nodes = set()

        
nodes_visited_so_far = list()    


def count_islands(graph):
    q = deque()
    island_counter = 0
    
    for node in graph.all_nodes():
        if node not in nodes_visited_so_far:
            island_counter += 1
            q.append(node)
            
            while q:
                n = q.popleft()
                for neighbor in graph.neighbors(n):
                    if neighbor not in nodes_visited_so_far:
                        q.append(neighbor)
                nodes_visited_so_far.append(n)
            
            q.clear()
    
    return island_counter


if __name__ == '__main__':
    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 0, 1, 1],
              [1, 0, 0, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1]]
    pprint(matrix, width=32)
    
    graph = GridAsGraph(matrix)
    print 'Number of islands(Union-Find): {}'.format(graph.count_islands())
    print 'Number of islands(BFS): {}'.format(count_islands(graph))
    
    print '***'.center(20)
    
    matrix = [[0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0]]
    pprint(matrix, width=32)
    
    graph = GridAsGraph(matrix)
    print 'Number of islands(Union-Find): {}'.format(graph.count_islands())
    print 'Number of islands(BFS): {}'.format(count_islands(graph))
