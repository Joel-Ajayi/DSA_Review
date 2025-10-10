from __future__ import annotations
import math
from typing import Optional, Any


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


class LinkedList:
    head:Optional["Node"]
    tail:Optional["Node"]
    len:int = 0
    
    def __init__(self, value:Optional[int] = None) -> None:
        new_node = None
        
        if value != None:
            new_node = Node(value)
            self.len = 1
        self.head = new_node
        self.tail = new_node
        
    def __str__(self) -> str:
        next_node = self.head
        link = 'head'
        while next_node is not None:
            link = f"{link} -> {next_node.data}"
            next_node = next_node.next
        
        link = f"{link} -> tail"
        return link
            
        
    def append(self, value):
        new_node = Node(value)
        self.len += 1
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
        
    def prepend(self, value):
        new_node = Node(value)
        self.len += 1
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def reverse(self):
        prev = None
        curr = self.head
            
        self.tail = prev
        
        while curr is not None:
            next_curr,curr.next = curr.next, prev
            prev = curr
            curr = next_curr
            if curr is not None:
                self.head = curr
                
    def get_mid_node(self):
        if self.len == 0:
            return 0
        
        mid = int(self.len/2 + 1) if self.len % 2 == 0 else math.ceil(self.len/2)
        
        return self.get(mid)
    
    def remove_duplicate(self):
        prev = None
        curr = self.head
        
        dic = {}
        while curr is not None:
            count = dic.get(curr.data, 0) + 1
            dic[curr.data] = count
            
            next = curr.next
            if count > 1:
                if prev is not None:
                    prev.next = next
                curr = next
            else:
                prev = curr
                curr = next
        
    def insert(self, index:int, value):
        new_node = Node(value)
        temp_node = self.head
        temp_index = 0
        self.len += 1
        
        if temp_node is None:
            self.head = new_node
            self.tail = new_node
            return
        
        insert_index = self.len + index if index < 0 else index

        while temp_node is not None:
            # insert at index 0
            if insert_index == 0:
                new_node.next = temp_node
                self.head = new_node
                return True
            
            if temp_index == insert_index - 1:
                new_node.next, temp_node.next = temp_node.next, new_node
                return True
            
            temp_node = temp_node.next
            temp_index += 1
        
        self.len -=1
        return False
    
    def search(self, target:int):
        curr_node = self.head
        curr_index = 0
        while curr_node is not None:
            if target == curr_node.data:
                return curr_index
            
            curr_node =curr_node.next
            curr_index += 1
        return -1
    
    def get(self, index:int):
        curr_node = self.head
        curr_index = 0
        get_index = self.len + index if index < 0 else index
        
        if get_index > self.len -1 or curr_index is None:
            return None
        
        while curr_node is not None:
            if curr_index == get_index:
                return curr_node
            
            curr_node = curr_node.next
            curr_index += 1
        
        return None
    
    def set(self, index:int, data:int):
        node  = self.get(index=index)
        if node:
            node.data = data
            return True
        
        return False
    
    def pop(self):
        temp_node = self.head
        
        if temp_node is None:
            return None

        while temp_node is not None:
            # only enters once when length is 1
            if self.len == 1:
                self.head = None
                self.tail = None
                self.len -= 1
                return temp_node
            
            if temp_node.next is self.tail:
                remove_node = temp_node.next
                temp_node.next = remove_node.next if remove_node else None 
                self.tail = temp_node
                self.len -= 1
                return remove_node

            temp_node = temp_node.next
        
        
        return None
    
    def remove(self, index:int):
        temp_node = self.head
        curr_index = 0
        
        remove_index = self.len + index if index < 0 else index
        
        if remove_index >= self.len or temp_node is None:
            return None

        while temp_node is not None:
            # only time it enters here if for index 0
            if self.len == 1:
                self.head = None
                self.tail = None
                self.len -= 1
                return temp_node
        
            if curr_index == remove_index - 1:
                remove_node = temp_node.next
                temp_node.next = remove_node.next if remove_node else None 
                if remove_node is self.tail:
                    self.tail = temp_node
                self.len -= 1
                return remove_node
        
            temp_node = temp_node.next
            curr_index += 1
        
        return None
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.len = 0
        
        
new_list = LinkedList()
new_list.append(10)
new_list.append(20)
new_list.append(30)
new_list.prepend(5)
new_list.insert(1, 7)
new_list.insert(4, 20)
new_list.set(-1, 55)
new_list.append(5)

# new_list.remove(-1)
# new_list.pop()
new_list.append(90)
print(new_list)

# new_list.reverse()

new_list.remove_duplicate()

print(new_list)