class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1 2 2 4 5 6 9 
        candidates.sort() # so that all duplicates are adjacent 

        print(candidates)

        def dfs(curList,i,total):
            if total==target:
                res.append(curList.copy())
                return
            if total>target or i>len(candidates):
                return
            
            for j in range(i,len(candidates)):
                # if duplicate num, at the same level 
                if candidates[j]==candidates[j-1] and j>i:
                    continue 
                curList.append(candidates[j])
                dfs(curList,j+1,total+candidates[j])
                curList.pop() 

        dfs([],0,0)
        return res
        