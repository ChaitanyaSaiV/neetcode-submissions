class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        self.graph = {}

        for i in range(n):
            self.graph[i] = []

        for edge in edges:
            a, b = edge
            self.graph[a].append(b)
            self.graph[b].append(a)
        
        count = 0
        for node in self.graph:
            if node not in self.visited:
                self.graphTraverse(node)
                count += 1
        
        return count
    
    def graphTraverse(self, node):
        if node in self.visited:
            return

        self.visited.add(node)
        for neighbor in self.graph[node]:
            self.graphTraverse(neighbor)
        
        return

