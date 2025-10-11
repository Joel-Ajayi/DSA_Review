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


class Tree:
    root: Node

    def __init__(self, data: int):
        self.root = Node(data)

    def preorderT(self, node: Optional["Node"] = None):
        if not node is None:
            print(f"{node.data} -> ")
            self.preorderT(node.left)
            self.preorderT(node.right)

    def inorder(self, node: Node):
        if node.left:
            self.inorder(node.left)

        print(f"{node.data} -> ")

        if node.right:
            self.inorder(node.right)

    def postorder(self, node: Optional["Node"] = None):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(f"{node.data} -> ")

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

    def getDeepestNode(self):
        if not self.root:
            return
        q = Queue[Node]()
        q.enqueue(self.root)
        while not q.is_empty():
            root = cast(Node, q.dequeue())
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

        return root

    def deleteDeepestNode(self):
        if not self.root:
            return
        q = Queue[Node]()
        q.enqueue(self.root)
        dNode = self.getDeepestNode()
        while not q.is_empty():
            curr_node = cast(Node, q.dequeue())
            if curr_node.left is not None:
                q.enqueue(curr_node.left)

            if curr_node.right is not None:
                q.enqueue(curr_node.right)

            if curr_node.left == dNode:
                curr_node.left = None
                break
            elif curr_node.right == dNode:
                curr_node.right = None
                break

        return dNode

    def search(self, value: int):
        q = Queue[Node]()
        q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            if not node:
                break

            if node.data == value:
                print(node.data)
                return node

            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)

    def insert(self, value: int):
        new_node = Node(value)
        q = Queue[Node]()
        q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            if not node:
                break

            if not node.left:
                node.left = new_node
                return "Inserted"

            if not node.right:
                node.right = new_node
                return "Inserted"

            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)

    def get_node_level(self, node: Optional["Node"], value: int, level: int = 1):
        if node is None:
            return -1

        if node.data == value:
            return level

        left_level = self.get_node_level(node.left, value, level + 1)
        if left_level != -1:
            return left_level

        right_level = self.get_node_level(node.right, value, level + 1)
        if right_level != -1:
            return right_level

        return -1


tree = Tree(1)
n3 = Node(3)
n2 = Node(2)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

tree.root.left = n2
n2.left = n4
n2.right = n5

n4.left = n9
n4.right = n10


tree.root.right = n3
n3.right = n7
n3.left = n6

print("O(n) space and time compexity")
print("Reorder Traversal")
tree.preorderT(tree.root)

print("Inorder Traversal")
tree.inorder(tree.root)

print("Post order Traversal")
tree.postorder(tree.root)
tree.insert(12)

print("Level order Traversal")
tree.levelorder()

print(tree.search(5))


print(tree.search(12))

tree.get_node_level(tree.root, 12)

print(tree.getDeepestNode())

print(tree.deleteDeepestNode())

print(tree.getDeepestNode())
