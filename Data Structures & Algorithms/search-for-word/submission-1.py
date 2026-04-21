class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenRow = len(board)
        lenCol = len(board[0])
        visited = set() 
        
        #use idx to track word -> only increment idx if past letters are correct
        def dfs(r,c,idx):
            if idx == len(word): 
                return True 
            if r>=lenRow or c>=lenCol or r<0 or c<0: 
                return False
            # if cur string is alr wrong return false
            if (r,c) in visited or board[r][c]!=word[idx]:
                return False 

            #explore 
            visited.add((r,c))
            found = (dfs(r+1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c-1,idx+1))
            visited.remove((r,c))

            return found
        
        for i in range(lenRow):
            for j in range(lenCol):
                if dfs(i,j,0):
                    return True
        return False
