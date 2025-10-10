from typing import Optional, Any


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

    def levelorder(self, node: Node):
        pass


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

print("Level order Traversal")
tree.postorder(tree.root)
