#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (67.54%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 33.1K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0
# 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 
# 
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 
# 
# 
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
# 
# 
# 
# 示例：
# 
# 输入： 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出：
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# 
# 进阶：
# 
# 
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
# 
# 
#

# @lc code=start
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 第一个循环在原矩阵内标记每个细胞的状态
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.check(board, i, j)
        # 第二个循环基于状态给细胞确定0还是1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] == 1 or board[i][j] == -2 else 0

    def check(self, board, i, j):
        cnt = 0
        left = max(j-1,0)
        right = min(j+1,len(board[i])-1)
        top = max(i-1,0)
        bottom = min(i+1,len(board)-1)
        for row in range(top, bottom+1):
            for col in range(left, right+1):
                cnt = cnt + 1 if board[row][col] == 1 or board[row][col] == -1 else cnt
        # 细胞状态：
        # 1 即 细胞本来是活的，周围有2或3个活细胞，保持1存活
        # -2 即 细胞本来是死的，周围有3个活细胞，从0复活成1
        # 0 即 细胞本来是死的，依然是死细胞，保持0死亡
        # -1 即 细胞本来是活的，周围活细胞少于2或大于3，从1死亡成0
        if board[i][j] == 1:
            state = 1 if cnt == 3 or cnt == 4 else -1 # 这里3=2+1和4=3+1是算上了本身也是个活细胞
        else:
            state = -2 if cnt == 3 else 0
        return state
        
# @lc code=end

