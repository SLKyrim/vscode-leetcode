#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.21%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 45.1K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start

class UnionFind:
    def __init__(self, index):
        self.roots = []
        for i in range(index):
            self.roots.append(i)
    
    def findRoot(self, index):
        # There must be a root in self.roots equals its own index
        while self.roots[index] != index:
            self.roots[index] = self.roots[self.roots[index]]
            index = self.roots[index]
        return index

    def union(self, index1, index2):
        root1 = self.findRoot(index1)
        root2 = self.findRoot(index2)
        if root1 != root2:
            self.roots[root1] = root2
    
    def isConnected(self, index1, index2):
        return self.findRoot(index1) == self.findRoot(index2)   

class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def xyTo1D(row, col):
            return row * cols + col
        
        uf = UnionFind(rows * cols + 1)
        # make the last position as a dummyNode connects the O on edge 
        dummyNode = rows * cols

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                        uf.union(xyTo1D(i, j), dummyNode)
                    else:
                        if i - 1 >= 0 and board[i - 1][j] == 'O':
                            uf.union(xyTo1D(i, j), xyTo1D(i - 1, j))
                        if i + 1 < rows and board[i + 1][j] == 'O':
                            uf.union(xyTo1D(i, j), xyTo1D(i + 1, j))
                        if j - 1 >= 0 and board[i][j - 1] == 'O':
                            uf.union(xyTo1D(i, j), xyTo1D(i, j - 1))
                        if j + 1 < cols and board[i][j + 1] == 'O':
                            uf.union(xyTo1D(i, j), xyTo1D(i, j + 1))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not uf.isConnected(xyTo1D(i, j), dummyNode):
                    board[i][j] = 'X'
        
# @lc code=end

