class TreeNode:

    def __init__(self, name):
        self.name = name
        self.parent
        self.left_child = None
        self.right_child = None
    
    def add_child(self, parent, child, is_left=True):
        if parent and child:
            if is_left:
                parent.left = child
            else:
                parent.right = child  
    
    
class Tree:

    def __init__(self, root):
        self.root = root
    

def find_nearest_common_ancestor(root, source, dest):
    if root:
        if root == source or root == dest:
            return root
        else:
            left_ancestor = find_nearest_common_ancestor(root.left, source, dest)
            right_ancestor = find_nearest_common_ancestor(root.right, source, dest)
            if left_ancestor and right_ancestor:
                return root
            else:
                return left_ancestor if left_ancestor else right_ancestor
    return None


def find_distance_from_ancestor(ancestor, node):
    if ancestor and node:
        if node == ancestor:
            return 0
        
        parent = node.parent
        hop = 1
        while(parent != ancestor):
            hop += 1
            parent = parent.parent
        return hop
            
    
def find_num_hops(tree, source, dest):
    nearest_common_ancestor = find_nearest_common_ancestor(tree.root, source, dest)
    distance_source = find_distance_from_ancestor(nearest_common_ancestor, source)
    distance_dest = find_distance_from_ancestor(nearest_common_ancestor, dest)
    return distance_source + distance_dest
        
