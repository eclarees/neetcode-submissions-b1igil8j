class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [] 
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))
        print(sorted_strs)

        seen = {} 
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in seen:
                seen[sorted_strs[i]].append(strs[i])
            else: 
                seen[sorted_strs[i]] = [strs[i]]
        print(seen)

        output = [] 
        for array in seen.values():
            output.append(array)

        return output


        