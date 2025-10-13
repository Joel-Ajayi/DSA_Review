from typing import Optional, cast
from enum import Enum


class HeapType(Enum):
    MINHEAP = "min"
    MAXHEAP = "max"


class BHeap:
    tree: list[Optional[int]]
    maxSize: int
    heapSize: int

    def __init__(self, max: int):
        self.tree = [None] * (max + 1)
        self.heapSize = 0
        self.maxSize = max + 1

    def peek(self):
        return self.tree[1]

    def size(self):
        return self.heapSize

    # O(n) for time and space is O(1)
    def levelorder(self):
        return " -> ".join([f"{i}" for i in self.tree if i is not None])

    # we use swapping here
    def insert(self, val: int):
        if self.heapSize + 1 == self.maxSize:
            return "max size"

        self.heapSize += 1
        self.tree[self.heapSize] = val
        self.heapifyFromButtom(self.heapSize)
        return "Value Inserted"

    # O(logN) for space and time
    def heapifyFromButtom(self, index: int, type: HeapType = HeapType.MINHEAP):
        if index <= 1:
            return

        is_even_index = index % 2
        parent_index = index // 2 if is_even_index == 0 else (index - 1) // 2
        swap = False
        parent = cast(int, self.tree[parent_index])
        child = cast(int, self.tree[index])

        swap = child < parent if type.value == HeapType.MINHEAP else child > parent

        if swap:
            self.tree[parent_index], self.tree[index] = child, parent
            self.heapifyFromButtom(parent_index, type)

    # O(logN) for space and time
    def heapifyFromTop(self, index: int, type: HeapType = HeapType.MAXHEAP):
        left_index = 2 * index
        right_index = 2 * index + 1

        if self.heapSize < left_index:
            return

        left_node = cast(int, self.tree[left_index])
        right_node = cast(int, self.tree[right_index])
        curr_node = cast(int, self.tree[index])

        if self.heapSize == left_index:
            # handle one node remaning
            swap = (
                curr_node > left_node
                if type.value == HeapType.MINHEAP
                else curr_node < left_node
            )
            if swap:
                self.tree[left_index], self.tree[index] = curr_node, left_node
        else:
            #  handle two nodes
            if type.value == HeapType.MINHEAP:
                swap_node = left_node if left_node < right_node else right_node
                swap_index = left_index if left_node < right_node else right_index
            else:
                swap_node = left_node if left_node > right_node else right_node
                swap_index = left_index if left_node > right_node else right_index

            swap = (
                swap_node < curr_node
                if type.value == HeapType.MINHEAP
                else swap_node > curr_node
            )
            if swap:
                self.tree[swap_index], self.tree[index] = curr_node, swap_node
                self.heapifyFromTop(swap_index, type)

        return

    # can only extract root node
    def extract(self, tree_root: Optional[int] = None):
        root = tree_root if tree_root is not None else self.tree[1]

        self.tree[1] = self.tree[self.heapSize]
        self.tree[self.heapSize] = None
        self.heapSize -= 1
        self.heapifyFromTop(1)
        return root

    def delete(self):
        self.tree = []
        self.heapSize = 0

    # for min heap
    def sort(self):
        # 1. insert data to the tree.
        # 2. next extratct data from the tree
        pass


bh = BHeap(9)
bh.insert(4)
bh.insert(5)
bh.insert(2)
bh.insert(1)
print(bh.extract())
print(bh.levelorder())
