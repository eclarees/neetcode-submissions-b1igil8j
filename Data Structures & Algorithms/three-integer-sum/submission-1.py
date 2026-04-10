class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() 
        for i in range(len(nums)-2):
            j = i+1 
            k = len(nums)-1 
            while j<k:
                total = nums[i] +nums[j]+nums[k]
                if total == 0:
                    if ([nums[i],nums[j],nums[k]]) not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    k-=1 
                    j+=1
                else:
                    if total > 0:
                        k-=1 
                    else: 
                        j+=1

        return ans

        