class Node:

    def __init__(self, value, Min):
        self.value = value
        self.min = Min

class MinStack:

    '''
    
    O(1) -> for all functions

    maintain min_variable, that gets invalidated everypop
    [21476,21476,21477,21477,-21478]

    '''

    def __init__(self):
        self.stack  = []
        self.min = 2 ** 31
       

    def push(self, value: int) -> None:
        
        self.min = min(value, self.min)
        self.stack.append(Node(value,self.min))
        

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Empty Stack")
        self.stack.pop()
        if not self.stack:
            self.min = 2**31
        else:
            self.min = self.getMin()
        

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Empty Stack")
        return self.stack[-1].value
    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Empty Stack")
        return self.stack[-1].min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()