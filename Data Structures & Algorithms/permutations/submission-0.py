class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
  
        def dfs(curList,remaining):
            if len(curList)==len(nums):
                res.append(curList.copy())
                return

            for i in range(len(remaining)):
                newRemaining = remaining[:i] + remaining[i+1:]
                curList.append(remaining[i])
                dfs(curList,newRemaining)
                curList.pop()
        dfs([],nums)
        return res

        # i=0                 i=1 
        # newR 2,3            newR 3 
        # dfs([1],[2,3]).     dfs([1,2])
        
        # dfs([1,2],[3])            

            



        