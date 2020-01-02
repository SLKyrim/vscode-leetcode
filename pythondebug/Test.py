# -*- coding: utf-8 -*-
"""
Created on 2019/12/27 17:07



Author: Long
"""


class Trie:
    class Node:
        def __init__(self):
            self.isEnd = False
            self.links = {}

        def containsKey(self, ch):
            return (ord(ch) - ord('a')) in self.links.keys()

        def put(self, ch, node):
            self.links[ord(ch) - ord('a')] = node

        def get(self, ch):
            return self.links[ord(ch) - ord('a')]

        def setEnd(self):
            self.isEnd = True

        def getEnd(self):
            return self.isEnd

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, self.Node())
            node = node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return False
        if not node.getEnd():
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return False
        return True


if __name__ == '__main__':
    s = Trie()
    s.insert("apple")
    print(s.search("apple"))