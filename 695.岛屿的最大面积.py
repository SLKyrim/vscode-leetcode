#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (58.79%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 34.2K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地)
# 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
# 
# 示例 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
# 
# 示例 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(row):
            for j in range(col):
                stack = [(i, j)]
                cnt = 0
                while stack:
                    xi, yj = stack.pop()
                    if xi < 0 or yj < 0 or xi == row or yj == col or grid[xi][yj] == 0:
                        continue
                    cnt += 1
                    grid[xi][yj] = 0 # 关键：访问过的位置置0，保证每个位置只访问一次
                    for dfs in direction:
                        nexti = xi + dfs[0]
                        nextj = yj + dfs[1]
                        stack.append((nexti, nextj))
                res = max(res, cnt)
        return res

# @lc code=end

