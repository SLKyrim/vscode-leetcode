#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (62.69%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 30.9K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
# 示例:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 
# 说明:
# 
# 
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
# 
# 
#

# @lc code=start
## Easy Understand Solution
# class Trie:

#     class Node:
#         def __init__(self):
#             self.isEnd = False
#             self.links = {}
            
#         def containsKey(self, ch):
#             return (ord(ch) - ord('a')) in self.links.keys()

#         def put(self, ch, node):
#             self.links[ord(ch) - ord('a')] = node
        
#         def get(self, ch):
#             return self.links[ord(ch) - ord('a')]

#         def setEnd(self):
#             self.isEnd = True
        
#         def getEnd(self):
#             return self.isEnd

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = self.Node()
        
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         node = self.root
#         for ch in word:
#             if not node.containsKey(ch):
#                 node.put(ch, self.Node())
#             node = node.get(ch)
#         node.setEnd()
        
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         node = self.root
#         for ch in word:
#             if node.containsKey(ch):
#                 node = node.get(ch)
#             else:
#                 return False
#         if not node.getEnd():
#             return False
#         return True

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         node = self.root
#         for ch in prefix:
#             if node.containsKey(ch):
#                 node = node.get(ch)
#             else:
#                 return False
#         return True

## Less Code (simplify) Solution
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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

