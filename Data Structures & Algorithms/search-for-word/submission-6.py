class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()
        self.i_length = len(board)
        self.j_length = len(board[0])
        for i in range(self.i_length):
            for j in range(self.j_length):
                self.visited = set()
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
    
    def dfs(self, board, word, word_index, i, j) -> bool:
        key = (i, j)
        if key in self.visited:
            return False

        if word_index == len(word):
            return True

        result = False
        self.visited.add(key)
        if 0 <= i < self.i_length and 0 <= j < self.j_length and board[i][j] == word[word_index]:
            
            neighbors = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)
            ]
            for neighbor in neighbors:
                a, b = neighbor
                if self.dfs(board, word, word_index + 1, a, b):
                    result = True
        self.visited.remove(key)
        return result

