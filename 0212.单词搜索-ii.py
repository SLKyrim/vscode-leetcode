#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.78%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 20.2K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' + '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 示例:
# 
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"]
# 
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
# 
# 提示:
# 
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
# 
# 
#

# @lc code=start
class Trie:
    def __init__(self):
        self.R = 26
        self.isEnd = False
        self.nodes = [None for i in range(self.R)]
        self.word = ""

    def insert(self, word):
        root = self
        for i in range(len(word)):
            if root.nodes[ord(word[i]) - ord('a')] == None:
                root.nodes[ord(word[i]) - ord('a')] = Trie()
            root = root.nodes[ord(word[i]) - ord('a')]
        root.isEnd = True
        root.word = word

    def search(self, board, res):
        root = self
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(res, board, root, i, j)
    
    def helper(self, res, board, root, i, j):
        if root.isEnd:
            root.isEnd = False
            res.append(root.word)
            return
        
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] != '#' and root.nodes[ord(board[i][j]) - ord('a')] != None:
                currRoot = root.nodes[ord(board[i][j]) - ord('a')]
                tmp = board[i][j]
                board[i][j] = '#'
                self.helper(res, board, currRoot, i + 1, j)
                self.helper(res, board, currRoot, i - 1, j)
                self.helper(res, board, currRoot, i, j + 1)
                self.helper(res, board, currRoot, i, j - 1)
                board[i][j] = tmp

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = list()
        if len(board) == 0 or len(words) == 0:
            return res        
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie.search(board, res)
        
        return res
# @lc code=end

