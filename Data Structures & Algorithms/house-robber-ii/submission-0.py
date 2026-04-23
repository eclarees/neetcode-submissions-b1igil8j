class Solution:
    def rob(self, nums: List[int]) -> int:
        length_nums=len(nums) 
        memo ={}
        if length_nums==1:
            return nums[0]
        def dfs(i,rob_first_flag):
            if i>=length_nums:
                return 0 
            if i==length_nums-1 and rob_first_flag==True:
                return 0 
            if (i, rob_first_flag) in memo:
                return memo[(i,rob_first_flag)]
            # do not rob and skip, rob and go to following house
            memo[(i,rob_first_flag)] = max(dfs(i+1,rob_first_flag), nums[i]+dfs(i+2,rob_first_flag))
            return memo[(i,rob_first_flag)]
        
        return max(dfs(0,True),dfs(1,False))

