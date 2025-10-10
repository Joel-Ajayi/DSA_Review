from typing import Optional, Any, cast
from collections import deque
from queue import Queue as IQueue
from multiprocessing import Queue as I2Queue

# append to end
class Queue:
    max_size:int
    items: list[Optional[int]]
    start:int
    top:int
    
    def __init__(self, max_size:int) -> None:
        self.items = cast(list[Optional[int]], [None] * max_size)
        self.max_size = max_size
        self.start = -1
        self.top = -1
        
    def enqueue(self, val:int):
        if self.isFull():
            return "Stack is full"
        
        # circular flow of max self.max_size-1
        self.top += -self.top if self.top + 1 == self.max_size else 1
        self.start = 0 if self.start == -1 else self.start
        self.items[self.top] = val
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.max_size:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Stack is empty"
        
        start = self.start
        firstEl = self.items[self.start]
        
        if start == self.top:
            self.start = -1
            self.top = -1
        else:
            # circular flow of max self.max_size-1
            self.start += -start if start + 1 == self.max_size else 1
        
        self.items[start] = None
        return firstEl
    
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty Stack"
        return ' -> '.join([str(val) for val in reversed(self.items)])
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        
        return self.items[self.start]
    
    def size(self):
        return len([var for var in self.items if var is not None])
    
    def isEmpty(self):
        return self.top == -1
    
    def deleteAll(self):
        self.items = cast(list[Optional[int]], [None] * self.max_size)
        self.start = -1
        self.top = -1
        

# everything is 0(1) complexity expect initialization of [None] * len list
# s = Queue(5)
# s.enqueue(20)
# s.enqueue(25)
# print(s.peek())
# s.dequeue()
# s.dequeue()
# print(s.peek())


# Inbuilt collections
q = deque(maxlen=5)
q.append(5)
q.append(10)
print(q)

# Inbuild Queue
q2 = IQueue()
q2.put(5)
q2.get()
q2.full()
q2.join()
