import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from typing import Optional, Any, cast

# Use absolute import so the module can be run as a script from the repo root.
from queue_lrn.linkedList_queue import Queue


class Node:
    left: Optional["Node"]
    right: Optional["Node"]
    data: int

    def __init__(
        self, data: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.data}"


class AVLTree:
    root: Optional[Node]

    def __init__(self, data: int):
        self.root = Node(data)

    def preorderT(self, node: Optional["Node"] = None):
        if not node is None:
            print(f"{node.data} -> ")
            self.preorderT(node.left)
            self.preorderT(node.right)

    # O(n) for space and time
    def inorder(self, node: Node):
        if node.left:
            self.inorder(node.left)

        print(f"{node.data} -> ")

        if node.right:
            self.inorder(node.right)

    # O(n) for space and time
    def postorder(self, node: Optional["Node"] = None):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(f"{node.data} -> ")

    # O(n) for space and time
    def levelorder(self):
        if not self.root:
            return
        q = Queue[Node]()
        q.enqueue(self.root)
        while not q.is_empty():
            root = cast(Node, q.dequeue())
            print(root.data)
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

    # O(logN) for space and time
    def insert(self, new_val: int, node: Optional["Node"] = None):
        if node is None:
            return Node(new_val)

        if new_val <= node.data:
            node.left = self.insert(new_val, node.left)
        else:
            node.right = self.insert(new_val, node.right)

        left_depth = self.get_tree_depth(node.left)
        right_depth = self.get_tree_depth(node.right)
        diff = left_depth - right_depth

        if abs(diff) > 1:
            left = cast(Node, node.left)
            right = cast(Node, node.right)

            # left side is deeper
            if diff > 1:
                # right rotate (left left case)
                if new_val <= left.data:
                    return self.rotateRight(node)
                # right rotate (left right case)
                if new_val > left.data:
                    node.left = self.rotateLeft(left)
                    return self.rotateRight(node)

            # right side is deeper
            if diff < -1:
                # right rotate (right right case)
                if new_val > right.data:
                    return self.rotateLeft(node)
                # right rotate (left right case)
                if new_val <= right.data:
                    node.right = self.rotateRight(right)
                    return self.rotateLeft(node)

        return node

    def getMinValNode(self, node: Node):
        if node is None or node.left is None:
            return node
        return self.getMinValNode(node.left)

    # O(logN) for space and time
    def delete(self, val: int, node: Optional["Node"] = None):
        if node is None:
            return None

        if val < node.data:
            node.left = self.delete(val, node.left)
        elif val > node.data:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            temp = self.getMinValNode(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right)

        left_depth = self.get_tree_depth(node.left)
        right_depth = self.get_tree_depth(node.right)
        diff = left_depth - right_depth

        if abs(diff) > 1:
            left = cast(Node, node.left)
            right = cast(Node, node.right)

            # left side is deeper
            if diff > 1:
                # right rotate (left left case)
                if val > left.data:
                    return self.rotateRight(node)
                # right rotate (left right case)
                if val <= left.data:
                    node.left = self.rotateLeft(left)
                    return self.rotateRight(node)

            # right side is deeper
            if diff < -1:
                # right rotate (right right case)
                if val <= right.data:
                    return self.rotateLeft(node)
                # right rotate (left right case)
                if val > right.data:
                    node.right = self.rotateRight(right)
                    return self.rotateLeft(node)

        return node

    # Left left case
    def rotateRight(self, node: Node):
        #        30                     20
        #      /                       /  \
        #     20      ->              10   30
        #    /  \                          /
        #  10    25                       25

        new_root = cast(Node, node.left)

        # since all right nodes of new node is less than current node
        # assign it
        node.left = new_root.right if new_root else None

        # set height to current node
        new_root.right = node
        return new_root

    def rotateLeft(self, node: Node):
        new_root = cast(Node, node.right)

        # since the new root nodes are greater than current node
        node.right = new_root.left if new_root else None

        new_root.left = node
        return new_root

    def get_tree_depth(self, node: Optional["Node"], level: int = 0):
        if node is None:
            return level - 1

        left_level = self.get_tree_depth(node.left, level + 1)
        right_level = self.get_tree_depth(node.right, level + 1)

        return left_level if left_level > right_level else right_level


avl = AVLTree(5)
avl.root = avl.insert(10, avl.root)
avl.root = avl.insert(15, avl.root)
avl.root = avl.insert(20, avl.root)
avl.root = avl.delete(15, avl.root)
avl.levelorder()
