#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
# https://leetcode-cn.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (58.54%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.3K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
# 
# 我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
# 
# 如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
# 
# 请返回封闭岛屿的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠            [1,1,1,1,1,1,1]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
# 
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            grid[r][c] = 1
            isOut = False
            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for x, y in directions:
                if 1 <= x < nr-1 and 1 <= y < nc-1 and grid[x][y] == 0:
                    if isOut:
                        dfs(x, y)
                    else:
                        isOut = dfs(x, y)
                if (0 <= x < nr and 0 <= y < nc) and (x == 0 or x == nr-1 or y == 0 or y == nc-1) and grid[x][y] == 0:
                    isOut = True
                    dfs(x, y)
            return isOut

        nr = len(grid)
        nc = len(grid[0])
        res = 0
        for i in range(1, nr-1):
            for j in range(1, nc-1):
                if grid[i][j] == 0:
                    res += 1
                    if dfs(i, j):
                        res -= 1
        return res
        
# @lc code=end

