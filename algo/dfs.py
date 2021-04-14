from ds.graph import Graph


def dfs(graph, source, discovered):
    for edge in graph.incident_edges(source):
        v = edge.opposite(source)
        if v not in discovered:
            discovered[v] = edge
            dfs(graph, v, discovered)

            
def construct_path(u, v, discovered):
    reverse_path = list() 
    if v in discovered:
        reverse_path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            reverse_path.append(parent)
            walk = parent
    return reverse_path[::-1]


def dfs_complete(graph):
    raise Exception('not implemented yet')


g = Graph()

a = g.insert_vertex('a') 
b = g.insert_vertex('b') 
c = g.insert_vertex('c') 
d = g.insert_vertex('d') 
e = g.insert_vertex('e') 
f = g.insert_vertex('f')

g.insert_edge(a, b)
g.insert_edge(a, c)
g.insert_edge(b, c)
g.insert_edge(b, d)
g.insert_edge(c, e)
g.insert_edge(d, f)
g.insert_edge(e, f)

if __name__ == '__main__':
    result = {a: None}
    dfs(g, a, result)
    print result
    
    print construct_path(a, f, result)
