class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        seen = dict(sorted(seen.items(), key=lambda item:item[1], reverse=True))

        print(seen)
        counter = 0 
        output = []
        for key,value in seen.items(): 
            output.append(key)
            counter +=1 
            if counter == k:
                return output 



        