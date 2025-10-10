from typing import Optional, Any, cast


class Node:
    """A node in a (singly) linked list.

    Attributes:
        data: stored value (number)
        next: optional reference to the next node
    """

    data: int
    next: Optional["Node"]

    def __init__(self, data: int, next: Optional["Node"] = None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:  # helpful for debugging
        return f"Node({self.data!r})"
    
from typing import Optional, Any, cast

class Stack:
    len:int
    top:Optional["Node"]
    
    def __init__(self) -> None:
        self.top = None
        self.len = 0
        
    def push(self, val:int):
        new_node = Node(val)
        self.len += 1
        if self.top:
           new_node.next = self.top
        self.top = new_node
            
    def pop(self):
        if self.isEmpty() or self.top is None:
            return "Stack is empty"
        
        self.len -= 1
        prev_head = self.top
        self.top = self.top.next
        return prev_head.data
    
    def __str__(self) -> str:
        next_node = self.top
        link = 'top'
        while next_node is not None:
            link = f"{link} -> {next_node.data}"
            next_node = next_node.next
        
        return link
    
    def peek(self):
        if self.isEmpty() or self.top is None:
            return "Stack is empty"
        
        return self.top.data
    
    def isEmpty(self):
        return self.len == 0
    
    def deleteAll(self):
        self.head = None
        self.len = 0
        

s = Stack()
s.push(20)
s.push(25)
print(s.peek())
print(s)