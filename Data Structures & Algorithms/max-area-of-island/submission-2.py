class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length , cols = len(grid), len(grid[0])
        maxArea = 0 
        visited = set()

        def dfs(i,j): # island found -> find edge of island and return area 
            if i<0 or j<0 or i>=length or j>=cols:
                return 0

            if (i,j) in visited:
                return 0
            if grid[i][j]==0 and (i,j) not in visited :
                return 0

            visited.add((i,j))
            return 1 + dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
            
        
        for i in range(length):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:

                    maxArea = max(maxArea,dfs(i,j))

        return maxArea

        