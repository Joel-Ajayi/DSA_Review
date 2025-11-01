# Used for strings
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofStr = False


from typing import cast


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if not char in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.endofStr = True

    def search(self, word):
        current = self.root
        for char in word:
            node = cast(TrieNode, current.children.get(char))

            if node == None:
                return True

            current = node

        return current.endofStr


t = Trie()
