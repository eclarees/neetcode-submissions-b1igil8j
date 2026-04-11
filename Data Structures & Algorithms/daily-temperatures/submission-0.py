class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for idx,temp in enumerate(temperatures):
            if not stack:
                stack.append([idx,temp])
            else: 
                print(stack)
                
                while len(stack)>0 and temp > stack[-1][1]: 
                    top_of_stack = stack.pop()
                    top_idx = top_of_stack[0]
                    top_temp = top_of_stack[1]
                    idx_diff = idx - top_idx 
                    ans[top_idx] = idx_diff
                    print(ans)
                stack.append([idx,temp])
                print(stack)

        return ans

        