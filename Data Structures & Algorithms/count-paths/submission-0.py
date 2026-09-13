class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        end_pos = (m - 1, n - 1)
        return self.traverse(0, 0, end_pos, {})
    
    def traverse(self, m, n, end_pos, memo):
        pos = (m, n)
        if pos in memo:
            return memo[pos]
        if pos == end_pos:
            return 1
        
        positions = self.get_positions(m, n, end_pos)

        path = 0
        for x, y in positions:
            path += self.traverse(x, y, end_pos, memo)

        memo[pos] = path

        return memo[pos]        

    def get_positions(self, m, n, end_pos):
        possible_positions = [
            (m + 1, n),
            (m, n + 1)
        ]

        in_bound_positions = []  # initialize list here

        end_m, end_n = end_pos

        for possible_position in possible_positions:
            x, y = possible_position
            if 0 <= x <= end_m and 0 <= y <= end_n:
                in_bound_positions.append(possible_position)
        
        return in_bound_positions


        
        