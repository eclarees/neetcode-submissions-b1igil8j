class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        length = len(grid)
        cols = len(grid[0])
        nums = 0 

        def dfs(i,j): # an island found -> just need to explore to edge of island 
            if i<0 or j<0 or i>=length or j>=cols:
                return 
            if (i,j) in visited:
                return
            if grid[i][j]=="0":
                return 
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

            

        for i in range(length):
            for j in range(cols):
                # scan every cell to see if its an island
                if grid[i][j]=="1" and (i,j) not in visited:
                    nums +=1 
                    dfs(i,j)
        return nums