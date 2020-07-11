#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (33.43%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 72K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
# 
# 示例1:
# 
# 
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# 示例2:
# 
# 
# 输入: 3
# 输出: False
# 
# 
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while c - i*i >= 0:
            cur = (c-i*i)**0.5
            if int(cur) - cur == 0:
                return True
            i += 1
        return False       
# @lc code=end

