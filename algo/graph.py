class Vertex:
    ''''Lightweight vertex structure for a graph'''
    __slots__ = '_element'

    def __init__(self, x):
        '''Do not call constructor directly. Use Graph's insert_vertex(x)''' 
        self._element = x

    def element(self):
        ''''Return element associated with this vertex''' 
        return self._element

    def __hash__(self):  # will allow vertex to be a map/set key 
        return hash(id(self))
    
    def __str__(self):
        return self._element
    
    def __repr__(self):
        return self.__str__()


class Edge:
    '''Lightweight edge structure for a graph'''
    __slots__ = '_origin' , '_destination' , '_element'

    def __init__(self, u, v, x):
        ''''Do not call constructor directly, use Graph's insert_edge(u,v,x)''' 
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        '''Return (u,v) tuple for vertices u and v'''
        return (self._origin, self._destination)

    def opposite(self, v):
        ''''Return the vertex that is opposite v on this edge''' 
        return self._destination if v is self._origin else self._origin

    def element(self):
        '''Return element associated with this edge''' 
        return self._element
    
    def __hash__(self):  # will allow edge to be a map/set key
        return hash((self._origin, self._destination))
    
    def __str__(self):
        return '-'.join((str(self._origin), str(self._destination)))
    
    def __repr__(self):
        return self.__str__()

    
class Graph:
    ''' Representation of a simple graph using adjacency map '''
    
    def __init__(self, directed=False):
        ''' Create an empty graph, undirected by default
            Graph is directed if the optional parameter directed set to True
        '''
        self._outgoing = dict()
        self._incoming = dict() if directed else self._outgoing  # only create if Graph is directed otherwise use alias
    
    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()
    
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
    
    def edges(self):
        return {edge for secondary_map in self._outgoing.values() for edge in secondary_map.values()}
    
    def get_edge(self, u, v):
    # return self._outgoing[u][v]
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        adjacency = self._outgoing if outgoing else self._incoming
        return len(adjacency[v])
    
    def incident_edges(self, v, outgoing=True):
        adjacency = self._outgoing if outgoing else self._incoming
        for edge in adjacency[v].values():
            yield edge
            
    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = dict()
        if self.is_directed():
            self._incoming[v] = dict()
        return v
    
    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._incoming[v][u] = e
        self._outgoing[u][v] = e
        
