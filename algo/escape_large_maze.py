from collections import namedtuple
import heapq

'''
    There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).
    We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of 
    blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).
    Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. 
    We are also not allowed to walk outside of the grid.
    
    Return true if and only if it is possible to reach the target square from the source square through a sequence 
    of valid moves.
    
    The catch here is the million by million grid, generally A* provides a very time efficient solution provided that
    the heuristic function is correctly implemented. But here A* won't work, A* based solution will fail on time limits.
'''


def is_escape_possible_using_using_a_star(blocked, source, target):
    Node = namedtuple('Node', ('x', 'y'))
    
    source, target, blocked = Node(*source), Node(*target), [Node(*b) for b in blocked]
    
    def get_neighbors(curr):
        return (node for node in map(Node, (curr.x - 1, curr.x + 1, curr.x, curr.x), (curr.y, curr.y, curr.y + 1, curr.y - 1)) 
                                        if 0 <= node.x < 10 ** 6 and 0 <= node.y < 10 ** 6 and node not in blocked)
    
    def heuristic(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)
   
    if (source and target and 
            0 <= source.x < 10 ** 6 and 0 <= source.y < 10 ** 6 and 
            0 <= target.x < 10 ** 6 and 0 <= target.y < 10 ** 6):
        if (source is target) or not blocked:
            return True
        
        frontier, cost_so_far = list(), dict()
        heapq.heappush(frontier, (0, source))
        cost_so_far[source] = 0
        
        while frontier:
            cost, curr_node = heapq.heappop(frontier)
            if curr_node is target: return True
            for neighbor in get_neighbors(curr_node):
                if (neighbor not in cost_so_far or
                        cost + 1 < cost_so_far[neighbor]):
                    cost_so_far[neighbor] = cost + 1
                    heapq.heappush(frontier, (cost_so_far[neighbor] + heuristic(neighbor, target), neighbor))
            
    return False


def is_escape_possible_using_dfs_enhanced(blocked, source, target):
    blocked = set(map(tuple, blocked))

    def dfs_helper(sx, sy, tx, ty):
        seen, frontier = {(sx, sy)}, list([(sx, sy)])
        while frontier:
            x, y = frontier.pop()
            if abs(x - sx) + abs(y - sy) > len(blocked) or (x, y) == (tx, ty): return True
            for nx, ny in map(tuple, map(lambda t1, t2: (t1, t2), (x - 1, x + 1, x, x), (y, y, y - 1, y + 1))):
                if 0 <= nx < 1e6 and  0 <= ny < 1e6 and (nx, ny) not in blocked and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    frontier.append((nx, ny))
        return  False
    
    return all([dfs_helper(source[0], source[1], target[0], target[1]),
                            dfs_helper(target[0], target[1], source[0], source[1])])                
                    
    
if __name__ == '__main__':
    blocked, source, target = [[0, 1], [1, 0]], [0, 0], [0, 2]
    print is_escape_possible_using_dfs_enhanced(blocked, source, target)
    
    blocked, source, target = [], [0, 0], [999999, 999999]
    print is_escape_possible_using_dfs_enhanced(blocked, source, target)
