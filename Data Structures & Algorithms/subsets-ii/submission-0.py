class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curList):
            if i>=len(nums):
                return

            #exploration 
            curList.append(nums[i])
            sorted_nums = sorted(curList)
            if sorted_nums not in res:
                res.append(sorted_nums)
            dfs(i+1,curList)

            curList.pop()
            dfs(i+1,curList)

        dfs(0,[])
        res.append([])
        return res

        # [] 
        # i = 0 [1] -> dfs: i=1 [1,2] -> i=2 [1,2,1] 
        # [] -> dfs: i=2 [2] -> dfs 