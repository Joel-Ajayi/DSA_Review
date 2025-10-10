from typing import Optional, Any, cast

# append to end
class Stack:
    len:int
    items:list[int] = []
    
    def __init__(self) -> None:
        self.items = []
        
    def push(self, val:int):
        self.items.append(val)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        
        return self.items.pop()
    
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty Stack"
        return ' -> '.join([str(val) for val in reversed(self.items)])
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def deleteAll(self):
        self.items = []
        

s = Stack()
s.push(20)
s.push(25)
print(s.peek())
s.pop()
print(s.peek())