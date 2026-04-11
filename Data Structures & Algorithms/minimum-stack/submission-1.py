class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min_stack = [] #track the running min up till cur index

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))


    def pop(self) -> None:
        if self.stack: 
            self.stack.pop() #remove the latest index from stack
            self.min_stack.pop() #remove the running min for latest index, reveals min from prev index

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
