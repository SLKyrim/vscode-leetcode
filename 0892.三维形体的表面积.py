#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (55.15%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 36.7K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
# 
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 
# 请你返回最终形体的表面积。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[[2]]
# 输出：10
# 
# 
# 示例 2：
# 
# 输入：[[1,2],[3,4]]
# 输出：34
# 
# 
# 示例 3：
# 
# 输入：[[1,0],[0,2]]
# 输出：16
# 
# 
# 示例 4：
# 
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 
# 
# 示例 5：
# 
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                height = grid[i][j] # 当前柱体的高度
                if height > 0: # 加这个条件，不然0高度的柱体会贡献2个上下表面积
                    res += 2 + 4 * height # 上下面积（2）+ 侧面积（4 * 高度）

                    # 减去柱体贴合表面积（低的柱体高度 * 2）
                    if i > 0:
                        # 减去与上面的柱体的贴合面积
                        res -= min(height, grid[i - 1][j]) * 2
                    if j > 0:
                        # 减去与左面的柱体的贴合面积
                        res -= min(height, grid[i][j - 1]) * 2
        return res
    
# @lc code=end

