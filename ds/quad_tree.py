
'''
    Quadtree the data structure for spatial indexing.
    In Quadtree every nodes have exactly four children. When the 
    number of points in a leaf reaches a specific threshold, the tree
    recursively divides.  
'''

import heapq
from itertools import islice
from math import sqrt 
from random import uniform

from matplotlib import patches

import matplotlib.pyplot as plt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        
class Node:

    def __init__(self, x0, y0, width, height, points, parent):
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        self.points = points
        self.parent = parent
        self.children = list()
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_points(self):
        return self.points
    
    
class QuadTree:

    def __init__(self, area_width, area_height, threshold, points):
        self.threshold = threshold
        self.points = points
        self.root = Node(0, 0, area_width, area_height, self.points, None)
        self.subdivide()
        
    def add_point(self, x, y):
        self.points.append(Point(x, y))
        
    def get_points(self):
        return self.points
    
    def subdivide(self):
        recursive_subdivide(self.root, self.threshold)
        
    def get_plot(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("Quadtree")
        a_sub_plot = fig.add_subplot(111)
        children = find_children_recursive(self.root)
        for n in children:
            a_sub_plot.add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        plt.plot([point.x for point in self.points], [point.y for point in self.points], 'ro')
        return plt
    
    def find_node(self, x, y):
        return recursive_find(self.root, x, y)


def recursive_find(node, x, y):
    if not (node.x0 <= x <= node.x0 + node.width
            and node.y0 <= y <= node.y0 + node.height): return None
            
    if not len(node.children): return node
    
    if in_left_half(node, x) and in_lower_half(node, y): return recursive_find(node.children[0], x, y)
    elif in_right_half(node, x) and in_lower_half(node, y): return recursive_find(node.children[1], x, y)
    elif in_right_half(node, x) and in_upper_half(node, y): return recursive_find(node.children[2], x, y)
    else: return recursive_find(node.children[3], x, y)


def in_left_half(node, x):
    w, _ = get_node_half_width_height(node)
    return node.x0 <= x <= node.x0 + w


def in_right_half(node, x):
    return not in_left_half(node, x)


def in_lower_half(node, y):
    _, h = get_node_half_width_height(node)
    return node.y0 <= y <= node.y0 + h


def in_upper_half(node, y):
    return not in_lower_half(node, y)


def recursive_subdivide(node, k):
    if len(node.points) <= k: return
    
    w, h = get_node_half_width_height(node)
    
    filtered_points_for_node = points_in_region(node.x0, node.y0, w, h, node.points)
    sw_node = Node(node.x0, node.y0, w, h, filtered_points_for_node, node)
    recursive_subdivide(sw_node, k)
    
    filtered_points_for_node = points_in_region(node.x0 + w, node.y0, w, h, node.points)
    se_node = Node(node.x0 + w, node.y0, w, h, filtered_points_for_node, node)
    recursive_subdivide(se_node, k)
    
    filtered_points_for_node = points_in_region(node.x0 + w, node.y0 + h, w, h, node.points)
    ne_node = Node(node.x0 + w, node.y0 + h, w, h, filtered_points_for_node, node)
    recursive_subdivide(ne_node, k)
    
    filtered_points_for_node = points_in_region(node.x0, node.y0 + h, w, h, node.points)
    nw_node = Node(node.x0, node.y0 + h, w, h, filtered_points_for_node, node)
    recursive_subdivide(nw_node, k)
    
    node.children = [sw_node, se_node, ne_node, nw_node]


def get_node_half_width_height(node):
    return float(node.get_width() / 2), float(node.get_height() / 2)

    
def points_in_region(x, y, w, h, points):
    return filter(lambda point: x <= point.x <= x + w and y <= point.y <= y + h, points)


def find_children_recursive(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children_recursive(child))
    return children


def get_k_closest_points(point, points, k):
    points_iter = iter(points)
    max_heap = [(-distance(point, curr_point), curr_point) for curr_point in islice(points_iter, k)]
    heapq.heapify(max_heap)
    curr_point = next(points_iter, None)
    while curr_point:
        heapq.heappushpop(max_heap, (-distance(point, curr_point), curr_point))
        curr_point = next(points_iter, None)
    
    return [item[1] for item in max_heap]


def distance(point_1, point_2):
    return sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


def find_k_neighboring_points(k, quad_tree, point):
    found_node = quad_tree.find_node(point.x, point.y)
    points = found_node.points
    while len(points) < k and found_node.parent:
        found_node = found_node.parent
        points = found_node.points
    if len(points) > k:
        points = get_k_closest_points(point, points, k)
        
    return points


if __name__ == '__main__':
    n = 200
    points = [Point(uniform(5, 10), uniform(3, 7)) for _ in range(n)]
    n = 200
    points.extend(Point(uniform(0, 10), uniform(0, 10)) for _ in range(n))
    quad_tree = QuadTree(10, 10, 15, points)

    k = 10
    my_location = Point(4, 6)
    neighboring_points = find_k_neighboring_points(k, quad_tree, my_location)
    
    plot = quad_tree.get_plot()
    plot.plot([point.x for point in neighboring_points], [point.y for point in neighboring_points],
                'go', label='{} neighboring points'.format(k))
    plot.plot(my_location.x, my_location.y, 'bx', label='my location')
    plot.legend()
    plot.show()
