from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in sorted(self.graph[node]):
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if not visited[node]:
                print(node, end=" ")
                visited[node] = True

                for neighbor in sorted(self.graph[node]):
                    if not visited[neighbor]:
                        queue.append(neighbor)

    def find_cycles(self, node, visited, stack):
        visited[node] = True
        stack.append(node)

        for neighbor in self.graph[node]:
            if neighbor in stack:
                print("Cycle:", " ".join(map(str, stack[stack.index(neighbor):] + [neighbor])))
            elif not visited[neighbor]:
                self.find_cycles(neighbor, visited, stack)

        stack.pop()

    def is_bipartite(self, start):
        color = [-1] * (max(self.graph) + 1)
        color[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbor in self.graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

        return True

def is_tree(graph):
    visited = [False] * (max(graph) + 1)

    def dfs(node):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    start_node = next(iter(graph))
    dfs(start_node)

    return all(visited)

# Example usage:
g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 2)

print("DFS:")
g.dfs(1, [False] * (max(g.graph) + 1))
print("\nBFS:")
g.bfs(1)
print("\nCycles:")
g.find_cycles(1, [False] * (max(g.graph) + 1), [])
print("\nIs Bipartite:", g.is_bipartite(1))
print("Is Tree:", is_tree(g.graph))
