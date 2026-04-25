class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal_idx = len(nums)-1  

        for idx in range(len(nums)-2,-1,-1): 
            if idx+nums[idx]>=goal_idx:
                goal_idx = idx 
                print(goal_idx)
        if goal_idx ==0:
            return True
        return False

        