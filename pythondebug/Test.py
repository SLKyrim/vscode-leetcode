# -*- coding: utf-8 -*-
"""
Created on 2019/12/27 17:07



Author: Long
"""

class Trie:
    def __init__(self):
        self.R = 26
        self.isEnd = False
        self.nodes = [None for i in range(self.R)]

    def insert(self, word):
        root = self
        for ch in word:
            if root.nodes[ord(ch) - ord('a')] == None:
                root.nodes[ord(ch) - ord('a')] = Trie()
            root = root.nodes[ord(ch) - ord('a')]
        root.isEnd = True

    def search(self, word):
        root = self
        for ch in word:
            if root.nodes[ord(ch) - ord('a')] == None:
                return False
            root = root.nodes[ord(ch) - ord('a')]
        return root.isEnd

    def startsWith(self, prefix):
        root = self
        for ch in prefix:
            if root.nodes[ord(ch) - ord('a')] == None:
                return False
            root = root.nodes[ord(ch) - ord('a')]
        return True


if __name__ == '__main__':
    s = Trie()
    s.insert("apple")
    print(s.search("app"))