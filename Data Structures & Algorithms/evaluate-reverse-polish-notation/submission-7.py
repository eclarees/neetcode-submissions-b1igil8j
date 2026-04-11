class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        
        for i in tokens: 
            if i!="+" and i!="-" and i!="*" and i!="/":
                stack.append(int(i))
                print(stack)
            else:
                num1 = stack.pop()
                num2 = stack.pop() 
                if i=="+":
                    ans = num1 +num2  
                elif i=="*":
                    ans = num1 *num2  
                elif i=="-":
                    ans = num2 -num1 
                else:
                    ans = int(num2/num1) 
                stack.append(ans)
                print(stack)
        return stack.pop()
        