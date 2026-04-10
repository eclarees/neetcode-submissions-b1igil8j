class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1 
        while i<j:
            print(numbers[i])
            print(numbers[j])
            sum_num = numbers[i]+numbers[j]
            if sum_num>target:
                j-=1 
            elif sum_num<target:
                i+=1 
            else:     
                return [i+1,j+1]