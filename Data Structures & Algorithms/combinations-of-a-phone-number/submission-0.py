class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            2: ["a","b","c"], 
            3: ["d","e","f"], 
            4: ["g","h","i"], 
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }
        res = [] 

        def dfs(i,curString):
            if len(curString) == len(digits):
                res.append(curString[:])
                return 
            if i>=len(digits):
                return 
            
            cur_digit = int(digits[i])
            for char in hashmap[cur_digit]:
                dfs(i+1,curString+char)
        if digits:
            dfs(0,"")
        return res
        
        
            

            