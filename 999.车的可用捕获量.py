#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 车的可用捕获量
#
# https://leetcode-cn.com/problems/available-captures-for-rook/description/
#
# algorithms
# Easy (65.32%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 12.7K
# Testcase Example:  '[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
#
# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符
# “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
# 
# 
# 车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
# 
# 返回车能够在一次移动中捕获到的卒的数量。
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# 输出：3
# 解释：
# 在本例中，车能够捕获所有的卒。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# 输出：0
# 解释：
# 象阻止了车捕获任何卒。
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# 输出：3
# 解释： 
# 车可以捕获位置 b5，d6 和 f5 的卒。
# 
# 
# 
# 
# 提示：
# 
# 
# board.length == board[i].length == 8
# board[i][j] 可以是 'R'，'.'，'B' 或 'p'
# 只有一个格子上存在 board[i][j] == 'R'
# 
# 
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = -1, -1
        for i in range(len(board)):
            try:
                col = board[i].index('R')
                row = i
                break
            except:
                continue
        res = 0
        tmp = row - 1
        while tmp >= 0:
            if board[tmp][col] == 'p':
                res += 1
                break
            if board[tmp][col] == 'B':
                break
            tmp -= 1
        tmp = row + 1
        while tmp < len(board):
            if board[tmp][col] == 'p':
                res += 1
                break
            if board[tmp][col] == 'B':
                break
            tmp += 1
        tmp = col - 1
        while tmp >= 0:
            if board[row][tmp] == 'p':
                res += 1
                break
            if board[row][tmp] == 'B':
                break
            tmp -= 1
        tmp = col + 1
        while tmp < len(board[0]):
            if board[row][tmp] == 'p':
                res += 1
                break
            if board[row][tmp] == 'B':
                break
            tmp += 1
        return res
        
# @lc code=end

