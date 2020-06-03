#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (43.67%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 10.8K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
# 
# 示例 1:
# 
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 1, 2]
# 输出: False
# 
# 
# 注意:
# 
# 
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
# 
# 
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:

        eps = 1e-6

        def dfs(tmp):
            if self.res:
                return 
            if len(tmp) == 1:
                if abs(24 - tmp[0]) < eps:
                    self.res = True
                return

            for i in range(len(tmp)):
                for j in range(i):
                    n1, n2 = tmp[i], tmp[j]
                    nex = [n1+n2, n1-n2, n2-n1, n1*n2]
                    if n1 != 0:
                        nex.append(n2/n1)
                    if n2 != 0:
                        nex.append(n1/n2)
                    
                    tmp.remove(n1)
                    tmp.remove(n2)
                    for n in nex:
                        tmp.append(n)
                        dfs(tmp)
                        tmp.pop() # 回溯1
                    # 回溯2
                    tmp.insert(j, n2)
                    tmp.insert(i, n1)
        
        self.res = False
        dfs(nums)
        return self.res

# @lc code=end

