class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs (curList,total,i):
            if total==target:
                res.append(curList.copy())
                return
            if total>target or i>=len(nums):
                return 
            
            # add num 
            curList.append(nums[i])
            dfs(curList, total+nums[i], i) #stay at index, reuse same num 

            # backtrack, and skip num
            curList.pop()
            dfs(curList, total,i+1)
        
        dfs([],0,0)
        return res 
