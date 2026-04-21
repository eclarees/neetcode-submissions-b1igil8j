class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited or board[r][c] != word[idx]:
                return False

            visited.add((r, c))
            found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                    dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
            visited.remove((r, c))  # backtrack
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False

            