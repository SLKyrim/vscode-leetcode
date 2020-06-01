#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stocj-iii/description/
#
# algorithms
# Hard (42.66%)
# Likes:    394
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 85.6K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # dp[i][j][0] 表示第i天未持有股票时的最大收益，且至多进行了j次买股票，由两种状态转移：
        # 1、第i-1天持有股票并在第i天卖掉，dp[i][j][0] = dp[i-1][j][1] + prices[i-1]
        # 2、第i-1天未持有股票，并休息，dp[i][j][0] = dp[i-1][j][0]
        # dp[i][j][1] 表示第i天持有股票时的最大收益，且至多进行了j次买股票，由两种状态转移：
        # 1、第i-1天未持有股票并在第i天买进，dp[i][j][1] = dp[i-1][j-1][0] - prices[i-1]
        # 2、第i-1天持有股票，并休息，dp[i][j][1] = dp[i-1][j][1]
        # 【注意】prices的索引要比dp的索引快一天，即prices[i-1]指的是第i天的价格
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0] * 2 for _ in range(2+1)] for _ in range(n+1)]
        for j in range(2+1):
            dp[0][j][1] = -prices[0] # 没有实际意义，为之后的循环逻辑正确而占位
        for i in range(1, n + 1):
            for j in range(1, 2+1):
                dp[i][j][0] = max(dp[i-1][j][1] + prices[i-1], dp[i-1][j][0])
                dp[i][j][1] = max(dp[i-1][j-1][0] - prices[i-1], dp[i-1][j][1])
        return dp[n][2][0]
# @lc code=end

