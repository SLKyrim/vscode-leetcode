#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode-cn.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (50.78%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 8K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
# 
# 移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
# 
# 返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释： 
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 
# 示例 2：
# 
# 输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# 所有行的大小都相同
# 
# 
#

# @lc code=start
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        # # 按正常岛屿DFS思路的做法
        # def dfs(r, c, cnt, isOut):
        #     A[r][c] = 0
        #     di = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        #     if isOut:
        #         for x, y in di:
        #             if 0 <= x < nr and 0 <= y < nc and A[x][y] == 1:
        #                 dfs(x, y, 0, isOut)
        #         return [0, isOut]
        #     for x, y in di:
        #         if 0 <= x < nr and 0 <= y < nc and A[x][y] == 1:
        #             if x == 0 or x == nr-1 or y == 0 or y == nc-1:
        #                 isOut = True
        #                 cnt = dfs(x, y, 0, isOut)[0]
        #             else:
        #                 cnt, isOut = dfs(x, y, cnt+1, isOut)
        #     return [cnt, isOut]

        # nr = len(A)
        # nc = len(A[0])
        # res = 0
        # for i in range(nr):
        #     for j in range(nc):
        #         if (i==0 or i==nr-1 or j==0 or j==nc-1) and A[i][j] == 1:
        #             dfs(i, j, 0, True)
        #         if A[i][j] == 1:
        #             res += dfs(i, j, 1, False)[0]
        # return res


        # 从周围的1开始DFS变为0，最后统计剩下的1的个数
        def dfs(r, c):
            A[r][c] = 0
            di = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for x, y in di:
                if 0 <= x < nr and 0 <= y < nc and A[x][y] == 1:
                        dfs(x, y)

        nr = len(A)
        nc = len(A[0])
        for i in range(nr):
            if A[i][0] == 1:
                dfs(i, 0)
            if A[i][nc-1] == 1:
                dfs(i, nc-1)
        for j in range(nc):
            if A[0][j] == 1:
                dfs(0, j)
            if A[nr-1][j] == 1:
                dfs(nr-1, j)
        res = 0
        for i in range(1, nr-1):
            for j in range(1, nc-1):
                if A[i][j] == 1:
                    res += 1
        return res

        
# @lc code=end

