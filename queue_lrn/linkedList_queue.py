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


class Queue:
    head: Optional["Node"]
    tail: Optional["Node"]
    len: int = 0

    def __init__(self, value: Optional[int] = None) -> None:
        new_node = None

        if value != None:
            new_node = Node(value)
            self.len = 1
        self.head = new_node
        self.tail = new_node

    def __str__(self) -> str:
        next_node = self.head
        link = "head"
        while next_node is not None:
            link = f"{link} -> {next_node.data}"
            next_node = next_node.next

        link = f"{link} -> tail"
        return link

    def enqueue(self, value):
        new_node = Node(value)
        self.len += 1

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        temp_node = self.head
        self.len -= 1

        if temp_node is None:
            return None

        if self.len == 0:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next

        return temp_node

    def peek(self) -> Optional[int]:
        """Return the value at the front of the queue without removing it."""
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return self.len == 0

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return self.len

    def delete_all(self) -> None:
        """Remove all elements from the queue."""
        self.head = None
        self.tail = None
        self.len = 0
