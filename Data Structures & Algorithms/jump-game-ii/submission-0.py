class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        l = r = 0 # window -> determine portion of arr used for BFS
        
        while r<len(nums)-1:
            farthest = 0 
            # increment window 
            for i in range(l,r+1):
                # get the furthest index it can jump to from current idx
                jump_to_idx = i + nums[i]
                farthest = max(farthest,jump_to_idx)
            # update window 
            l = r+1 
            r = farthest 
            # increment result -> number of jumps
            res +=1 
        return res

        