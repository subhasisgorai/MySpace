from collections import defaultdict


class Graph:

    def __init__(self, vertices_count):
        self.graph = defaultdict(list)
        self.vertices_count = vertices_count
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def __topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.__topological_sort_util(i, visited, stack)
        stack.insert(0, v)
        
    def __simple_dfs(self, u, visited, result):
        visited[u] = True
        result.append(u)
        for v in self.graph[u]:
            if visited[v] == False:
                self.__simple_dfs(v, visited, result)
                
    def simple_dfs_non_recursive(self, start_node):
        stack = list()
        result = list()
        visited = [False] * self.vertices_count
        
        stack.append(start_node)
        
        while stack:
            u = stack.pop()
            result.append(u)
            visited[u] = True
            if self.graph[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        stack.append(v)
        print 'non-recursive DFS result: {}'.format(result)
        
    def topological_sort(self):
        visited = [False] * self.vertices_count
        stack = []
        for i in range(self.vertices_count):
            if visited[i] == False:
                self.__topological_sort_util(i, visited, stack)
        print 'Topological Sort order: {}'.format(stack)
    
    def dfs(self, u):
        result = []
        visited = [False] * self.vertices_count
        self.__simple_dfs(u, visited, result)
        print 'recursive DFS result: {}'.format(result)
        
    def bfs(self, u):
        queue = list()
        result = list()
        visited = [False] * self.vertices_count
        
        queue.append(u)
        
        while queue:
            u = queue.pop(0)
            result.append(u)
            visited[u] = True
            if self.graph[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True
                            
        print 'BFS result: {}'.format(result)

        
if __name__ == '__main__':
    g = Graph(8)
       
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(4, 7)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    g.add_edge(4, 5)

#     g = Graph(5)
#     g.add_edge(0, 1)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#      
#     g.add_edge(3, 4)
    
    g.topological_sort()
    g.dfs(0)
    g.simple_dfs_non_recursive(0)
    g.bfs(0)
    
