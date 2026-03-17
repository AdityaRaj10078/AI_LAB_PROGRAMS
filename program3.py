from collections import deque

class Graph:
    def __init__(self):
        
        self.graph = {}

    def add_edge(self, u, v):
       
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

   
    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
            print("DFS Recursive Traversal:", end=" ")

        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

        
        if len(visited) == len(self.graph):
            print()

   
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        print("DFS Iterative Traversal:", end=" ")

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print()



if __name__ == "__main__":
    g = Graph()

    # Adding edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

  
    g.graph.setdefault('D', [])
    g.graph.setdefault('F', [])

    print("Graph Adjacency List:")
    for node in g.graph:
        print(f"{node} -> {g.graph[node]}")

    print()

    g.bfs('A')
    g.dfs_recursive('A')
    g.dfs_iterative('A')