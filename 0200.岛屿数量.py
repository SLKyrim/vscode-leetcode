#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (46.09%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    46.2K
# Total Submissions: 99.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给定一个由 '1'（陆地）和
# '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
# 
# 示例 1:
# 
# 输入:
# 11110
# 11010
# 11000
# 00000
# 
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# 11000
# 11000
# 00100
# 00011
# 
# 输出: 3
# 
# 
#

# @lc code=start

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            grid[r][c] = 0
            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] # 当前节点上下左右四个方向
            for x, y in directions:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    dfs(x, y) # 向当前节点上下左右方向DFS，将当前岛屿的所有1换为0
        
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        res = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res


# 并查集
# class UnionFind:
#     def __init__(self, index):
#         self.roots = []
#         for i in range(index):
#             self.roots.append(i)
    
#     def findRoot(self, index):
#         # There must be a root in self.roots equals its own index
#         while self.roots[index] != index:
#             self.roots[index] = self.roots[self.roots[index]]
#             index = self.roots[index]
#         return index

#     def union(self, index1, index2):
#         root1 = self.findRoot(index1)
#         root2 = self.findRoot(index2)
#         if root1 != root2:
#             self.roots[root1] = root2
    
#     def isConnected(self, index1, index2):
#         return self.findRoot(index1) == self.findRoot(index2)   

#     def getRoots(self):
#         for i in range(len(self.roots)):
#             self.roots[i] = self.findRoot(i)
#         return self.roots

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         rows = len(grid)
#         cols = len(grid[0])

#         def xyTo1D(row, col):
#             return row * cols + col

#         uf = UnionFind(rows * cols + 1)
#         # make the last position as a dummyNode presents 0 (water) 
#         dummyNode = rows * cols

#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == "0":
#                     uf.union(xyTo1D(i, j), dummyNode)
#                 else:
#                     if i - 1 >= 0 and grid[i - 1][j] == "1":
#                         uf.union(xyTo1D(i, j), xyTo1D(i - 1, j))
#                     if i + 1 < rows and grid[i + 1][j] == "1":
#                         uf.union(xyTo1D(i, j), xyTo1D(i + 1, j))
#                     if j - 1 >= 0 and grid[i][j - 1] == "1":
#                         uf.union(xyTo1D(i, j), xyTo1D(i, j - 1))
#                     if j + 1 < cols and grid[i][j + 1] == "1":
#                         uf.union(xyTo1D(i, j), xyTo1D(i, j + 1))
        
#         roots = uf.getRoots()
#         return len(set(roots)) - 1

# @lc code=end

