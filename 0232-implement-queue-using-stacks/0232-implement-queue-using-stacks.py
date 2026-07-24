class MyQueue:

    '''
     <-[ ] <-

     [1,2,3]


    
    '''

    def __init__(self):
        self.top = []
        self.bottom = []

    def push(self, x: int) -> None:
        
        self.top.append(x)
    
    def move_elements(self):
        if not self.bottom:

            while self.top:
                self.bottom.append(self.top.pop())
        
    def pop(self) -> int:
        if self.empty():
            raise IndexError("Empty Queue")
        self.move_elements()

        return self.bottom.pop()
    def peek(self) -> int:
        if self.empty():
            raise IndexError("Empty Queue")
        if not self.bottom:
            return self.top[0]
        return self.bottom[-1]

    def empty(self) -> bool:
        return not self.top and not self.bottom 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()