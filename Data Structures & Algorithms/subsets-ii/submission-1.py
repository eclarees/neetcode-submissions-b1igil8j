class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort input array -> so that duplicates are next to each other
        nums.sort()

        def dfs(i, curList): 
            # cur index reach end of nums -> finish exploring
            if i==len(nums): 
                res.append(curList.copy()) 
                return
            
            # explore
            ## all subsets that include nums[i]
            curList.append(nums[i])
            dfs(i+1,curList)
            
            ## all subsets that does not include nums[i]
            curList.pop()
            ## as long as i in bound and it has duplicates next to it -> increase i
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1 
            dfs(i+1,curList) 

        dfs(0,[])
        return res
            
