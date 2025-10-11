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


class BSTTree:
    root: Node

    def __init__(self, data: int):
        self.root = Node(data)

    # o(logn) for space and time
    def insert(self, val: Node | int, node: Optional["Node"] = None):
        new_node = val if type(val) == Node else Node(cast(int, val))
        curr_node = self.root if node is None else node

        if curr_node is not None:
            # left
            if new_node.data <= curr_node.data:
                if curr_node.left is not None:
                    self.insert(new_node, curr_node.left)
                else:
                    curr_node.left = new_node
            # right
            else:
                if curr_node.right is not None:
                    self.insert(new_node, curr_node.right)
                else:
                    curr_node.right = new_node

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

    # O(n) for space and time
    def levelorder(self):
        if not self.root:
            return
        q = Queue[Node]()
        q.enqueue(self.root)
        out = ""
        while not q.is_empty():
            root = cast(Node, q.dequeue())
            out += f"{root.data} -> "
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

        return out

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

    # O(logn) for space and time
    def search(self, val: int, node: Optional["Node"] = None):
        curr_node = self.root if node is None else node

        if curr_node is not None:
            if curr_node.data == val:
                print("Found")
                return

            if val <= curr_node.data:
                if curr_node.left is not None:
                    self.search(val, curr_node.left)
                    return
            else:
                if curr_node.right is not None:
                    self.search(val, curr_node.right)
                    return

        print("Not Found")

    # o(logn) for space and time
    def delete_node(self, val: int, curr_node: Optional["Node"]):
        if curr_node is None:
            return curr_node

        if val == curr_node.data:
            if curr_node.left is None:
                temp = curr_node.right
                curr_node = None
                return temp

            if curr_node.right is None:
                temp = curr_node.left
                curr_node = None
                return temp

            # if node has two children, replace this node with min node
            # then delete the min node
            temp = self.getMinNode(curr_node.right)
            curr_node.data = temp.data
            curr_node.right = self.delete_node(temp.data, curr_node.right)
        elif val < curr_node.data:
            curr_node.left = self.delete_node(val, curr_node.left)
        else:
            curr_node.right = self.delete_node(val, curr_node.right)

        return curr_node

    def getMinNode(self, parent: Node):
        currNode = parent
        while currNode.left:
            currNode = currNode.left
        return currNode

    def get_node_depth(self, node: Optional["Node"], value: int, level: int = 0):
        if node is None:
            return -1

        if node.data == value:
            return level

        correct_level = -1
        if value < node.data:
            correct_level = self.get_node_depth(node.left, value, level + 1)
        else:
            correct_level = self.get_node_depth(node.right, value, level + 1)

        return correct_level

    def get_tree_depth(self, node: Optional["Node"], level: int = 0):
        if node is None:
            return level - 1

        left_level = self.get_tree_depth(node.left, level + 1)
        right_level = self.get_tree_depth(node.right, level + 1)

        return left_level if left_level > right_level else right_level


bst = BSTTree(70)

bst.insert(90)
bst.insert(50)
bst.insert(60)
bst.insert(30)
bst.insert(40)
bst.insert(80)
bst.insert(100)
bst.insert(20)
#
print(bst.levelorder())

bst.delete_node(70, bst.root)

print(bst.levelorder())

print(bst.get_node_depth(bst.root, 40))

print(bst.get_tree_depth(bst.root))
