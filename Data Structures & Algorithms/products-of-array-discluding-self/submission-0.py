class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [] #prefix product
        arr2 = [] #suffix product

        prod = 1
        for i in nums: 
            prod *=i 
            arr1.append(prod)
        print(arr1)
        prod = 1
        for j in nums[::-1]:
            prod *= j 
            arr2.insert(0,prod)
        print(arr2)

        res = [] 
        length = len(nums)
        for i in range(length): 
            if i==0: 
                prod = arr2[i+1]
            elif i==len(nums)-1: 
                prod = arr1[i-1]
            else: 
                prod = arr2[i+1]*arr1[i-1]
            res.append(prod)
        return res

