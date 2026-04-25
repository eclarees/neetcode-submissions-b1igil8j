class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = [0]*len(nums)
        maxSum[0] = nums[0]

        for i in range(1,len(maxSum)):
            maxSum[i] = max(nums[i],nums[i]+maxSum[i-1])
        print(maxSum)
        return max(maxSum)
