from typing import Optional, TypeVar, Generic

# Generic type for the data stored inside a Node
T = TypeVar("T")


class Node(Generic[T]):
    """A node in a (singly) linked list.

    Attributes:
        data: stored value (number)
        next: optional reference to the next node
    """

    data: T
    next: Optional["Node[T]"]

    def __init__(self, data: T, next: Optional["Node[T]"] = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:  # helpful for debugging
        return f"Node({self.data!r})"


class Queue(Generic[T]):
    head: Optional[Node[T]]
    tail: Optional[Node[T]]
    len: int = 0

    def __init__(self, value: Optional[T] = None) -> None:
        new_node: Optional[Node[T]] = None

        if value is not None:
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

    def enqueue(self, value: T) -> None:
        new_node = Node(value)

        if self.tail is None:
            # empty queue
            self.head = new_node
            self.tail = new_node
            self.len = 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.len += 1

    def dequeue(self) -> Optional[T]:
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next
        self.len -= 1
        if self.head is None:
            self.tail = None

        return value

    def peek(self) -> Optional[T]:
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
