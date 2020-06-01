#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (53.11%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 48.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # dp[i][0] 表示第i天未持有股票时的最大收益，由两种状态转移：
        # 1、第i-1天持有股票并在第i天卖掉，dp[i][0] = dp[i-1][1] + prices[i-1]
        # 2、第i-1天未持有股票，并休息，dp[i][0] = dp[i-1][0]
        # dp[i][1] 表示第i天持有股票时的最大收益，同样由两种状态转移：
        # 1、第i-2天未持有股票并在第i天买进，dp[i][1] = dp[i-2][0] - prices[i-1]，因为有1天冷冻期，故需要从第i-2天的状态转移
        # 2、第i-1天持有股票，并休息，dp[i][1] = dp[i-1][1]
        # 【注意】prices的索引要比dp的索引快一天，即prices[i-1]指的是第i天的价格
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n + 1)]
        # dp[0][0] = 0
        dp[0][1] = 0 - prices[0] # 没有实际意义，为之后的循环逻辑正确而占位
        # dp[1][0] = 0
        dp[1][1] = 0 - prices[0] # 有实际意义，表示第1天时持有股票的最大收益
        # dp[2][0] = max(dp[1][1] + prices[1], dp[1][0])
        # dp[2][1] = max(dp[0][0] - prices[1], dp[1][1])
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i-1][1] + prices[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])
        return dp[n][0]
        
# @lc code=end

