'''
    Reference: https://www.redblobgames.com/pathfinding/a-star/introduction.html
    Points to note:
        1. Moving through cells not always needs same degree of effort/cost.
            Unless otherwise specified, default cost moving through a cell is 1.
            Dictionary non_unit_cost_map in the graph constructor is to override the unit cost.
        2. inaccessible_cells collection in the constructor argument lists down the inaccessible cells. 
'''
from collections import namedtuple
from collections import deque
import heapq

NodeTup = namedtuple('Node', ('x', 'y', 'cost')) 


def Node(x, y, cost=1):
    return NodeTup(x, y, cost)


class GridAsGraph:
    
    def __init__(self, m, n,
                    diagonal_movement_allowed=False,
                    inaccessible_cells=[],
                    non_unit_cost_map=dict()):
        self.all_nodes = list()
        self.diagonal_movement_allowed = diagonal_movement_allowed
        
        for x in range(m):
            for y in range(n):
                if (x, y) not in inaccessible_cells:
                    self.all_nodes.append(Node(x, y) 
                                          if (x, y) not in non_unit_cost_map 
                                          else Node(x, y, non_unit_cost_map[x, y]))
                
    def neighbors(self, current_node):
        if not self.diagonal_movement_allowed:
            return (node for node in map(Node, (current_node.x - 1, current_node.x + 1, current_node.x, current_node.x),
                       (current_node.y, current_node.y, current_node.y + 1, current_node.y - 1)) if node in self.all_nodes)
        else:
            return (node for node in map(Node, (current_node.x - 1, current_node.x - 1, current_node.x - 1,
                                                    current_node.x, current_node.x,
                                                    current_node.x + 1, current_node.x + 1, current_node.x + 1),
                                                (current_node.y - 1 , current_node.y, current_node.y + 1,
                                                    current_node.y - 1, current_node.y + 1,
                                                    current_node.y - 1, current_node.y, current_node.y + 1)) if node in self.all_nodes)


came_from = dict()


def trace_route(source, destination):
    current = destination
    stack = list()
    while current and current is not source:
        stack.append(current)
        if current in came_from:
            current = came_from[current]
    
    path = tuple(stack[i] for i in range(len(stack) - 1, -1, -1))
    return path


def bfs_path_finding(graph, source, destination):
    q = deque()
    came_from.clear()
    
    q.append(source)
    came_from[source] = None
    
    while q:
        node = q.popleft()
        if node is destination:
            break  # early exit if reached destination
        for neighbor in graph.neighbors(node):
            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = node
    
    route = trace_route(source, destination)            
    return len(route), route


# If the weights/costs of all the cells are not uniform, the
# BFS path finding won't work
def dijkstra_path_finding(graph, source, destination):
    priority_q = []
    came_from.clear()
    cost_to_reach = dict()
    
    heapq.heappush(priority_q, (0, source))
    cost_to_reach[source] = 0
    came_from[source] = None
    
    while priority_q:
        cost, node = heapq.heappop(priority_q)
        if node is destination:
            break
        
        for neighbor in graph.neighbors(node):
            if (neighbor not in cost_to_reach or 
                    cost + neighbor.cost < cost_to_reach[neighbor]):
                heapq.heappush(priority_q, (cost + neighbor.cost, neighbor))
                cost_to_reach[neighbor] = cost + neighbor.cost
                came_from[neighbor] = node
    
    return cost_to_reach[destination], trace_route(source, destination)

'''
    The BFS or Dijkstra Path Finding the frontier moves in all directions, 
    which could be inefficient as generally path finding involves one source
    and one destination vertices.
    If we are solving single source shortest distances to all vertices kind 
    of problem then BFS or Dijkstra make more sense.
    Let's make the frontier expands more towards the goal more than any other
    directions. Firstly, let's define a heuristic function that tells us how close
    we are to the destination.
      
'''


def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def heuristic_search(graph, source, destination):
    priority_q = list()
    came_from.clear()
    
    heapq.heappush(priority_q, (0, source))
    came_from[source] = None
    
    while priority_q:
        _, node = heapq.heappop(priority_q)
        
        if node is destination:
            break
        
        for neighbor in graph.neighbors(node):
            if neighbor not in came_from:
                heapq.heappush(priority_q, (heuristic(neighbor, destination), neighbor))
                came_from[neighbor] = node
    
    route = trace_route(source, destination)
    return sum([node.cost for node in route]), route


# Heuristic Search is faster for terrain with less obstacles,
# but it is not great and may not be accurate as well in the presence
# of significant obstacles.
# So Dijkstra is good and works well to find the shortest path but it 
# wastes time exploring in directions that are not promising, on the contrary,
# Greedy Best First Search (the heuristic one) explores in promising directions
# but the the final path may not be the shortest.
# A* algorithm comes for rescue here, which is both accurate and does not wastes 
# bandwidth exploring in wrong directions. It takes both the actual distance from start 
# and the estimated distance to the destination in consideration.
def a_star(graph, source, destination):
    priority_queue = list()
    cost_so_far = dict()
    came_from.clear()
    
    heapq.heappush(priority_queue, (0, source))
    cost_so_far[source] = 0
    came_from[source] = None
    
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if node is destination:
            break
        
        for neighbor in graph.neighbors(node):
            if (neighbor not in cost_so_far or 
                    cost + neighbor.cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = cost + neighbor.cost
                heapq.heappush(
                                priority_queue,
                                (cost_so_far[neighbor] + heuristic(neighbor, destination), neighbor)
                               )
                
                came_from[neighbor] = node
                
    route = trace_route(source, destination)
    return sum([node.cost for node in route]), route 


def test_path_finding_algos():
    g = GridAsGraph(5, 4)
    
    path = bfs_path_finding(g, Node(4, 0), Node(0, 3))
    print 'BFS: {}'.format(path)

    path = dijkstra_path_finding(g, Node(4, 0), Node(0, 3))
    print 'Dijkstra: {}'.format(path)
    
    graph_non_uniform_terrain = GridAsGraph(5, 4, diagonal_movement_allowed=True, non_unit_cost_map={(1, 2): 5})

    path = dijkstra_path_finding(graph_non_uniform_terrain, Node(4, 0), Node(0, 3))
    print 'Dijkstra: {}'.format(path)
    
    path = heuristic_search(graph_non_uniform_terrain, Node(4, 0), Node(0, 3))
    print 'Heuristic: {}'.format(path)
    
    graph_with_barrier = GridAsGraph(5, 4,
                                     diagonal_movement_allowed=True,
                                     inaccessible_cells=[(1, 1), (1, 2), (2, 2), (3, 2)])
    
    path = dijkstra_path_finding(graph_with_barrier, Node(4, 0), Node(0, 3))
    print 'Dijkstra: {}'.format(path)
    
    path = heuristic_search(graph_with_barrier, Node(4, 0), Node(0, 3))
    print 'Heuristic: {}'.format(path)
    
    path = a_star(graph_with_barrier, Node(4, 0), Node(0, 3))
    print 'A*: {}'.format(path)
    
    final_graph = GridAsGraph(5, 8, diagonal_movement_allowed=True,
                                non_unit_cost_map={(0, 3): 15, (2 , 3): 20},
                                inaccessible_cells=[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                                                         (2, 6), (3, 6), (3, 5), (3, 4), (3, 2), (4, 2)])
    path = a_star(final_graph, Node(4, 0), Node(0, 7))
    print 'A*: {}'.format(path)


if __name__ == '__main__':
    test_path_finding_algos()
    
