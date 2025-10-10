from typing import Optional, Any, cast

class Node:
    """A node in a (singly) linked list.

    Attributes:
        data: stored value (number)
        next: optional reference to the next node
    """

    data: int
    next: Optional["Node"]
    prev: Optional["Node"]

    def __init__(self, data: int, next: Optional["Node"] = None, prev: Optional["Node"] = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:  # helpful for debugging
        return f"Node({self.data!r})"


class CDLinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    len:int
    
    def __init__(self, val:Optional[int]=None) -> None:
        if val is None:
            self.len = 0
            self.head = None
            self.tail = None
            return
        
        new_node = Node(val)
        self.len = 1
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
    
    def append(self, val: int):
        new_node = Node(val)
        self.len += 1
        
        if self.tail is None or self.head is None:
            self.len = 1
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return new_node
        
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail = new_node
        self.head.prev = new_node
        
        
    def get_valid_index(self, index:int, is_insert = True):
        cascade = 1 if is_insert else 0
        new_index = self.len + index + cascade if index < 0 else index
        
        if new_index < 0 or (new_index > self.len if is_insert else new_index >= self.len):
            if not (index == 0 and self.len == 0):
                return -1
        
        return new_index
    
    def insert(self, index:int, val:int):
        insert_index = self.get_valid_index(index)
        if insert_index == -1:
            raise Exception("Bad Index")
        
        new_node = Node(val)
        self.len += 1
        
        if self.len == 0:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return new_node
        
        curr_node = self.head
        for i in range(insert_index+1):
            if curr_node is None:
                return
            
            if insert_index == 0:
                self.prepend(val)
            elif i == insert_index -1:
                new_node.next = curr_node.next
                new_node.prev = curr_node
                curr_node.next = new_node
                
                if self.tail is curr_node:
                    self.tail = new_node
                
            curr_node = curr_node.next
                
                
    def remove(self, index:int):
        remove_index = self.get_valid_index(index, False)
        if remove_index == -1:
            raise Exception("Bad Index")
        
        self.len -= 1
        if self.len == 0:
            self.head = None
            self.tail = None
        
        curr_node = self.head
        for i in range(remove_index+1):
            if curr_node is None or self.tail is None:
                return
            
            if remove_index == 0:
                new_head = cast(Node, curr_node.next)
                new_head.prev = self.tail
                self.tail.next = new_head
                self.head = new_head
                return curr_node
                
            if i == remove_index -1:
                remove_node = cast(Node,curr_node.next)
                
                if self.tail is remove_node:
                    self.tail = curr_node
                    curr_node.next = self.head
                else:
                    next_node = cast(Node,remove_node.next) 
                    next_node.prev = curr_node
                    curr_node.next = next_node 
                
                return remove_node
            curr_node = curr_node.next
            
        
    def prepend(self, val: int):
        new_node = Node(val)
        self.len += 1
        
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return new_node
        
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = self.tail
        self.head = new_node
        self.tail.next = new_node
        
    def get(self, index:int):
        get_index = self.get_valid_index(index, False)
        if get_index == -1:
            raise Exception("Bad Index")
        
        curr_node = self.head
        for i in range(get_index+1):
            if i == get_index:
                return curr_node
            
            curr_node = None if curr_node is None else  curr_node.next
    
    def __str__(self) -> str:
        out = ''
        curr_node = self.head
        for _ in range(self.len):
            if curr_node is None:
                break
            
            if curr_node is self.tail and curr_node is self.head:
               out += f"head({curr_node.data}) <-> tail({curr_node.data})"
               break
            
            if curr_node is self.head:
               out += f"head({curr_node.data})"
            elif curr_node is self.tail:
               out += f" <-> tail({curr_node.data})"
            else:
                out += f" <-> {curr_node.data}"
            
            curr_node = curr_node.next
               
        return out

cdll = CDLinkedList(8)
cdll.append(9)
cdll.prepend(2)
cdll.insert(-1, 105)
cdll.insert(1, 43)
print(cdll)
cdll.remove(4)
print(cdll)
