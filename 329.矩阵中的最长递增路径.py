#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (41.15%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 42.9K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 
# 示例 1:
# 
# 输入: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2:
# 
# 输入: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
#

# @lc code=start
import collections

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        self.r, self.c = len(matrix), len(matrix[0])
        memo = [[0] * self.c for _ in range(self.r)]

        def dfs(r, c):
            if memo[r][c] > 0:
                return memo[r][c]
            di = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            res = 1
            for x, y in di:
                if 0 <= x < self.r and 0 <= y < self.c and matrix[x][y] > matrix[r][c]:
                    res = max(res, dfs(x, y) + 1)
            memo[r][c] = res
            return res

        res = 0
        for i in range(self.r):
            for j in range(self.c):
                res = max(res, dfs(i, j))
        return res
 
# @lc code=end

