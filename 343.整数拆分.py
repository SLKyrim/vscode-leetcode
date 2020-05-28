#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (55.91%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    27.2K
# Total Submissions: 48.6K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0 for i in range(n + 1)] # dp[i]表示拆分i可以获得的最大乘积
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i // 2 + 1):
                # i的拆分有两种：
                # 1、j*dp[i-j],其中dp[i-j]为(i-j)的拆分
                # 2、j*(i-j),此时(i-j)本身比(i-j)的拆分dp[i-j]要大
                # P.S.：j的上界为i//2+1是因为j和(i-j)的取值是对称的，只需讨论一半即可
                dp[i] = max(dp[i], j * dp[i-j], j * (i-j))
        return dp[n]
# @lc code=end

