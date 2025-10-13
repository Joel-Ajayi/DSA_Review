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

    def __init__(
        self, data: int, next: Optional["Node"] = None, prev: Optional["Node"] = None
    ):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:  # helpful for debugging
        return f"Node({self.data!r})"


class DLinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    len: int

    def __init__(self, val: Optional[int] = None) -> None:
        if val is None:
            self.len = 0
            self.head = None
            self.tail = None
            return

        new_node = Node(val)
        self.len = 1
        self.head = new_node
        self.tail = new_node

    def append(self, val: int):
        new_node = Node(val)
        self.len += 1

        if self.tail is None:
            self.len = 1
            self.head = new_node
            self.tail = new_node
            return new_node

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, val: int):
        new_node = Node(val)
        self.len += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def get(self, index: int):
        get_index = self.get_valid_int(index)

        is_from_tail = False if get_index < (self.len // 2) else True
        start = 0
        stop = get_index
        step = 1
        temp_node = self.tail if is_from_tail else self.head

        if is_from_tail:
            start = self.len - 1
            stop = get_index - 1
            step = -1

        for curr_index in range(start, stop, step):
            if curr_index == get_index:
                return temp_node
            temp_node = cast(Node, temp_node.prev if is_from_tail else temp_node.next)

    def get_valid_int(self, index: int, is_insert=True):
        cascade = 1 if is_insert else 0
        insert_index = self.len + index + cascade if index < 0 else index
        if insert_index < 0 or insert_index > self.len:
            if not (self.len == 0 and insert_index == 0):
                return -1

        return insert_index

    def insert(self, index: int, val: int):
        insert_index = self.get_valid_int(index)
        if insert_index == -1:
            raise Exception("Invalid index")

        new_node = Node(val)
        self.len += 1
        if self.len == 0:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
            return new_node

        curr_node = self.head
        for i in range(insert_index + 1):
            if curr_node is None:
                return

            if insert_index == 0:
                new_node.next = curr_node
                curr_node.prev = new_node
                self.head = new_node
                break

            if i == insert_index - 1:
                new_node.next = curr_node.next
                new_node.prev = curr_node
                curr_node.next = new_node

                if self.tail is curr_node:
                    self.tail = new_node

            curr_node = curr_node.next

    def remove(self, index: int):
        remove_index = self.get_valid_int(index, is_insert=True)
        if remove_index == -1:
            raise Exception("Invalid index")

        self.len -= 1
        if self.len == 0 and self.tail:
            removed_node = self.head
            self.tail = None
            self.head = None
            return removed_node

        curr_node = self.head
        for i in range(remove_index + 1):
            if curr_node is None:
                return

            if remove_index == 0:
                prev_head = self.head
                new_head = cast(Node, curr_node.next)
                new_head.prev = None
                self.head = new_head
                return prev_head

            if i == remove_index - 1:
                removed_node = cast(Node, curr_node.next)

                if self.tail is removed_node:
                    curr_node.next = None
                    self.tail = curr_node
                else:
                    next_node = cast(Node, removed_node.next)
                    curr_node.next = next_node
                    next_node.prev = curr_node
                return removed_node

            curr_node = curr_node.next

    def __str__(self) -> str:
        out = ""
        curr_node = self.head
        while curr_node is not None:
            out += f" -> {curr_node.data}"
            curr_node = curr_node.next

        return out

    def reverse(self) -> None:
        """Reverse the linked list in-place."""
        if self.head is None or self.tail is None:
            return

        curr_node = self.head
        prev_node = curr_node.prev
        self.tail = curr_node
        for _ in range(self.len):
            if curr_node is None:
                return

            next_node = curr_node.next

            curr_node.next, curr_node.prev = prev_node, next_node

            curr_node, prev_node = next_node, curr_node

        self.head = prev_node


dll = DLinkedList(8)
dll.append(9)
# dll.prepend(6)
# dll.append(10)
# dll.append(20)
# dll.reverse()
dll.insert(2, 100)
dll.insert(0, 2)
dll.insert(-1, 58)
print(dll)
dll.reverse()
print(dll)
