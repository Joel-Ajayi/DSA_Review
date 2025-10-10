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


class CLinkedList:
    head: Optional[Node]
    tail: Optional["Node"]
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
        new_node.next = new_node
        
    def append(self, val:int):
        new_node = Node(val)
        self.len += 1
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return;
        
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head
        
    def prepend(self, val:int):
        new_node = Node(val)
        self.len += 1
        
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return;
        
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node
        
    def insert(self, index:int, val:int):
        insert_index = self.len + index if index < 0 else index
        if insert_index >= self.len or insert_index < 0 and self.len != 0:
            raise Exception("Invalid index")
        
        new_node = Node(val)
        self.len += 1
        temp_node = self.head
        if self.len == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return;
        
        curr_index = 0
        
        while curr_index <= insert_index and temp_node and self.tail:
            if insert_index == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
                break
                
            if curr_index == insert_index - 1:
                new_node.next = temp_node.next
                temp_node.next = new_node
                
                if self.tail is temp_node:
                    self.tail = new_node
                break
                
            curr_index += 1
            temp_node = temp_node.next
            
    def get(self, index:int):
        get_index = self.len + index if index < 0 else index
        if get_index >= self.len or get_index < 0:
            raise Exception("Invalid index")
        
        temp_node = self.head
        curr_index = 0
        
        while curr_index < get_index and temp_node:
            temp_node = temp_node.next
            curr_index += 1
        
        return temp_node
    
    def pop(self):
        return self.remove(-1)

    def remove(self, index:int):
        remove_index = self.len + index if index < 0 else index
        if remove_index >= self.len or remove_index < 0:
            raise Exception("Invalid index")
        
        temp_node = self.head
        curr_index = 0
        self.len -= 1
        if self.len == 0 and self.tail:
            self.tail.next = None
            self.head = None
            self.tail = None
        
        while curr_index <= remove_index and temp_node and self.tail:
            if remove_index == 0:
                self.tail.next = temp_node.next
                self.head = temp_node.next
                return temp_node
            
            if curr_index == remove_index - 1:
                remove_node = cast(Node,temp_node.next) 
                temp_node.next = remove_node.next
                
                if self.tail is remove_node:
                    self.tail = temp_node
                return remove_node
            
            curr_index += 1
            temp_node = temp_node.next
    
    def delete(self):
        if self.tail:
            self.tail.next = None
            self.head = None
            self.tail = None
            self.len = 0
        
            
    def __str__(self) -> str:
        curr = self.head
        out = ""
        curr_index = 0
        while curr_index < self.len and curr is not None:
            if curr is self.head and curr is self.tail:
                out = f"head({curr.data}) -> tail({curr.data})"
                break
            
            out += f" -> tail({curr.data}) -> head({cast(Any, curr.next).data})" if curr is self.tail else f"head({curr.data})" if curr is self.head else f" -> {curr.data}"
            curr = None if curr is self.tail else curr.next
            curr_index += 1
        return out
                    
                  
            
            
            
list = CLinkedList()
list.append(10)
list.prepend(2)
list.insert(0, 50)
list.append(21)

print(list)

list.pop()
print(list)
print(list)
        
    