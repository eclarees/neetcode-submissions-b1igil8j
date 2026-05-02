class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums.copy()
        minProd = nums.copy() 

        for i in range(1,len(nums)):
            if nums[i]<0:
                minProd[i] = min(minProd[i],nums[i]*maxProd[i-1])
                maxProd[i] = max(maxProd[i],nums[i]*minProd[i-1])
            else:
                minProd[i] = min(minProd[i],nums[i]*minProd[i-1])
                maxProd[i] = max(maxProd[i],nums[i]*maxProd[i-1])
            
        return max(maxProd)
