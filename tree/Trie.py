# Used for strings
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofStr = False

    pass


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root


t = Trie()
