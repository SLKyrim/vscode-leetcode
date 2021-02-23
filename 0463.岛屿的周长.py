#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (64.19%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 19.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
# 
# 
# 
# 示例 :
# 
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# 输出: 16
# 
# 解释: 它的周长是下面图片中的 16 个黄色的边：
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 在原grid四周加0边缘
        tmp = [[0 for i in range(len(grid[0]) + 2)] for i in range(len(grid) + 2)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp[i + 1][j + 1] = grid[i][j]
        
        # 遍历加边缘后的中间的原grid，统计每个1四周0的个数
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if tmp[i + 1][j + 1] == 1:
                    if tmp[i + 1][j] == 0:
                        res += 1
                    if tmp[i + 1][j + 2] == 0:
                        res += 1
                    if tmp[i][j + 1] == 0:
                        res += 1
                    if tmp[i + 2][j + 1] == 0:
                        res += 1
        
        return res
        
# @lc code=end

