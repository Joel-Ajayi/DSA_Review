import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from typing import Optional, Any, cast

# Use absolute import so the module can be run as a script from the repo root.
from queue_lrn.linkedList_queue import Queue


class Tree:
    tree: list[Optional[int]]
    lastUsedIndex: int
    maxSize: int

    def __init__(self, max: int):
        self.tree = [None] * max
        self.lastUsedIndex = 0
        self.maxSize = max

    def insert(self, val: int):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The tree is full"

        self.lastUsedIndex += 1
        self.tree[self.lastUsedIndex] = val
        return "The value has been inserted"

    def preorder(self, i=1):
        if i >= self.maxSize:
            return

        print(self.tree[i])
        left_index = 2 * i
        right_index = (2 * i) + 1
        self.preorder(left_index)
        self.preorder(right_index)

    def inorder(self, i=1):
        if i >= self.maxSize:
            return

        left_index = 2 * i
        right_index = (2 * i) + 1
        self.preorder(left_index)
        print(self.tree[i])
        self.preorder(right_index)

    def postorder(self, i=1):
        if i >= self.maxSize:
            return

        left_index = 2 * i
        right_index = (2 * i) + 1
        self.preorder(left_index)
        self.preorder(right_index)
        print(self.tree[i])

    def levelorder(self):
        for i in range(1, self.lastUsedIndex + 1):
            print(self.tree[i])


tree = Tree(10)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(9)
tree.insert(10)


# tree.preorder()

tree.levelorder()
