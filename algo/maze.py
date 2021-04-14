from collections import namedtuple


def has_path(maze, start, destination):
    if maze:

        def initialize_nodes():
            for i in range(len(maze)):
                for j in range(len(maze[0])):
                    if maze[i][j] == 0:
                        all_nodes.append(Cell(i, j))
                        
        def get_neighbors(node):
            neighbors = zip([node for node in map(Cell, (node.x - 1, node.x + 1, node.x, node.x),
                            (node.y, node.y, node.y + 1, node.y - 1))], (LEFT, RIGHT, UP, DOWN))
            return [zipped for zipped in neighbors if zipped[0] in all_nodes]
        
        def path_finder(node, in_direction):
            next_node = Cell(node.x + shift_with_direction[in_direction][0],
                                node.y + shift_with_direction[in_direction][1])
            if next_node in all_nodes:
                if next_node not in from_node:
                    from_node[next_node] = node
                    return path_finder(next_node, in_direction)
            else:
                if node is Cell(destination[0], destination[1]):
                    return True
                
            if all([neighbor[0] in from_node for neighbor in get_neighbors(node)]): 
                return False
            else:
                return any([path_finder(*neighbor) for neighbor in get_neighbors(node)])
        
        RIGHT, LEFT, UP, DOWN = range(4)
        shift_with_direction = ((0, 1), (0, -1), (-1, 0), (1, 0))
        all_nodes = list()
        Cell = namedtuple('Cell', ('x', 'y'))
        from_node = dict()
        
        initialize_nodes()
        return path_finder(Cell(start[0], start[1]), DOWN)

    
if __name__ == '__main__':
    print(has_path([[0, 0, 1, 0, 0], 
                    [0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0], 
                    [1, 1, 0, 1, 1], 
                    [0, 0, 0, 0, 0]], 
                [0, 4], [4, 4]))
