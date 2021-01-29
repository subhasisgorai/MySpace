from algo.graph import Graph


def bfs(graph, source, discovered):
    level = [source]
    while len(level) > 0:
        next_level = list()
        for u in level:
            for e in graph.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


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

result = {a: None}
bfs(g, a, result)
print result
                
