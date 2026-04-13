class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(curList,i,total):
            if total==target:
                res.append(curList.copy())
                return 
            if i>=len(nums) or total>target: 
                return 
            
            #exploration 
            # add cur nums[i] to list, and total , continue using nums[i]
            curList.append(nums[i])
            dfs(curList,i,total+nums[i])

            # dont add cur nums[i],  move to next index 
            # remove nums[i]
            curList.pop()
            dfs(curList,i+1,total)

            
        dfs([],0,0)
        return res