from collections import deque
from collections import namedtuple
from pprint import pprint

from ds.union_find import Partition
from timeit import repeat

Node = namedtuple('Node', ('x', 'y'))


class GridAsGraph:
    __slots__ = '_all_nodes'

    def __init__(self, grid):
        if grid:
            self._all_nodes = [Node(x, y) for x in range(len(grid)) 
                                for y in range(len(grid[0])) 
                                if grid[x][y] == 1]

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

        
def count_islands(graph):
    q = deque()
    island_counter = 0
    nodes_visited_so_far = list() 
    
    for node in graph.all_nodes():
        if node not in nodes_visited_so_far:
            island_counter += 1
            q.append(node)
            
            while q:
                n = q.popleft()
                nodes_visited_so_far.append(n)
                for neighbor in graph.neighbors(n):
                    if neighbor not in nodes_visited_so_far:
                        q.append(neighbor)
            
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
    
    print '***'.center(20)
    
    matrix = [[1, 1, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    pprint(matrix, width=32)
    graph = GridAsGraph(matrix)
    print 'Number of islands(Union-Find): {}'.format(graph.count_islands())
    print 'Number of islands(BFS): {}'.format(count_islands(graph))
    
    print '***'.center(20)
    
    print '\n'
    print ' Performance Check '.center(30, '-')
    
    SETUP_CODE = '''
from algo.islands import GridAsGraph
from algo.islands import count_islands

matrix = [[1, 1, 1, 1, 0],
          [1, 1, 0, 1, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0]]
graph = GridAsGraph(matrix)
    
    '''
    print 'Using Union-Find: {}'.format(repeat(stmt="graph.count_islands()", setup = SETUP_CODE, number=100, repeat=3))
    print 'Using BFS: {}'.format(repeat(stmt="count_islands(graph)", setup = SETUP_CODE, number=100, repeat=3))
    
