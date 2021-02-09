import collections
from pprint import pprint

Shape = collections.namedtuple('Shape', ('id', 'coordinates'))


def hash_function(self):
    return hash(self.id)


Shape.__hash__ = hash_function


def count_num_shapes(matrix):
    if not matrix:
        return 0
    
    coordinate_shape_mapping = dict()   

    def merge_shapes():
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    current_shape = coordinate_shape_mapping[(i, j)]
                    for temp_ord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if (0 <= temp_ord[0] < len(matrix)
                            and 0 <= temp_ord[1] < len(matrix[0])):
                            if matrix[temp_ord[0]][temp_ord[1]] == 1:
                                temp_shape = coordinate_shape_mapping[(temp_ord[0], temp_ord[1])]
                                new_shape = Shape(current_shape.id + '_' + temp_shape.id,
                                                  current_shape.coordinates.union(temp_shape.coordinates))
                                coordinate_shape_mapping[(i, j)] = coordinate_shape_mapping[(temp_ord[0], temp_ord[1])] = new_shape
                                temp_shape = None
                    current_shape = None
       
    def build_initial_shapes(): 
        id_counter = 0
       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    id_counter += 1
                    coordinates = set([(i, j)])
                    shape = Shape(str(id_counter), coordinates)
                    coordinate_shape_mapping[(i, j)] = shape
    
    build_initial_shapes()
    merge_shapes()
   
    final_shapes = set(coordinate_shape_mapping.values())
    return len(final_shapes)


if __name__ == '__main__':
    matrix = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
    pprint(matrix, width=32)
    print count_num_shapes(matrix)
