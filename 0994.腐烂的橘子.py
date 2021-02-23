#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.17%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 21.6K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 
# 
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 
# 
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 
# 
# 示例 3：
# 
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
# 
# 
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        visited = [[False for i in range(col)] for i in range(row)] # 记录坐标是否被访问过
        stack = [[x, y] for x in range(row) for y in range(col) if grid[x][y] == 2] # 记录腐烂橘子的坐标
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        res = 0
        while True:
            stack_next = list()
            while stack:
                rot_x, rot_y = stack.pop()
                for direction in directions:
                    visit_x, visit_y = rot_x + direction[0], rot_y + direction[1]
                    if 0 <= visit_x < row and 0 <= visit_y < col:
                        if visited[visit_x][visit_y] == False:
                            if grid[visit_x][visit_y] == 1:
                                grid[visit_x][visit_y] = 2
                                visited[visit_x][visit_y] = True
                                stack_next.append([visit_x, visit_y])
            if not stack_next:
                break
            res += 1
            stack = stack_next
        return -1 if [True for x in range(row) for y in range(col) if grid[x][y] == 1] else res


# @lc code=end

