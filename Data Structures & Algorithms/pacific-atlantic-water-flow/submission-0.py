class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.row_length = len(heights)
        self.col_length = len(heights[0])
        self.pac = set()
        self.atl = set()

        for c in range(self.col_length):
            self.dfs(heights, 0, c, heights[0][c], self.pac)
            self.dfs(heights, self.row_length - 1, c, heights[self.row_length - 1][c], self.atl)
        
        for r in range(self.row_length):
            self.dfs(heights, r, 0, heights[r][0], self.pac)
            self.dfs(heights, r, self.col_length - 1, heights[r][self.col_length - 1], self.atl)
        
        result = []
        for r in range(self.row_length):
            for c in range(self.col_length):
                key = (r, c)
                if key in self.atl and key in self.pac:
                    result.append(key)
        return result


    def dfs(self, heights, r, c, prev_height,visit):
        key = (r, c)
        if key in visit:
            return
        if r < 0 or c < 0:
            return

        if r >= self.row_length or c >= self.col_length:
            return

        if heights[r][c] < prev_height:
            return
        
        visit.add(key)

        self.dfs(heights, r + 1, c, heights[r][c], visit)
        self.dfs(heights, r - 1, c, heights[r][c], visit)
        self.dfs(heights, r, c + 1, heights[r][c], visit)
        self.dfs(heights, r, c - 1, heights[r][c], visit)
        return

