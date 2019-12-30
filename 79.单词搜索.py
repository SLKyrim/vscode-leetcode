#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (39.40%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 76.2K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        # cache the visit state of the board : 0 - unvisited; 1 - visited
        self.visited = [[]]
        # cache the matched number
        self.correctLen = 0 

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        self.visited = [[0 for i in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.helper(board, rows, cols, word, i, j):
                    return True
        return False

    ## start searching from point (i, j)
    def helper(self, board, rows, cols, word, i, j):
        if self.correctLen == len(word):
            return True
        
        res = False

        if 0 <= i < rows and 0 <= j < cols and self.visited[i][j] == 0 and board[i][j] == word[self.correctLen]:
            self.correctLen += 1
            self.visited[i][j] = 1
            res = self.helper(board, rows, cols, word, i - 1, j) or \
                  self.helper(board, rows, cols, word, i + 1, j) or \
                  self.helper(board, rows, cols, word, i, j - 1) or \
                  self.helper(board, rows, cols, word, i, j + 1)
            if res == False:
                self.correctLen -= 1
                self.visited[i][j] = 0
        
        return res
    
# @lc code=end

