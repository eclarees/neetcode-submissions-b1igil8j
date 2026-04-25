class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def form_int(num):
            res = 0
            power = 0
            for char in num[::-1]:
                cur_num = int(char)*pow(10,power)
                power+=1 
                res += cur_num
            return res
            
        num1_int = form_int(num1)
        num2_int = form_int(num2)
        print(num1_int,num2_int)
        ans = num1_int*num2_int 
        return str(ans)

        