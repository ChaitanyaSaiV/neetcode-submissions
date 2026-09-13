class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = (i, j)
                if key not in self.visited and grid[i][j] == "1":
                    self.traverseGraph(grid, i, j)
                    count += 1
        return count
    
    def traverseGraph(self, grid, i, j):
        key = (i, j)
        if key in self.visited:
            return
        self.visited.add(key)
        neighbors = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ]
        for neighbor in neighbors:
            a, b = neighbor
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == "1":
                self.traverseGraph(grid, a, b)
        return
