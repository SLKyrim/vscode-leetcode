#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (64.84%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 28.6K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 
# 返回获得利润的最大值。
# 
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
# 
# 示例 1:
# 
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 注意:
# 
# 
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # DP
        # dp[i][0] 表示第i天未持有股票时的最大收益，由两种状态转移：
        # 1、第i-1天持有股票并在第i天卖掉，dp[i][0] = dp[i-1][1] + prices[i-1]
        # 2、第i-1天未持有股票，并休息，dp[i][0] = dp[i-1][0]
        # dp[i][1] 表示第i天持有股票时的最大收益，同样由两种状态转移：
        # 1、第i-1天未持有股票并在第i天买进，dp[i][1] = dp[i-1][0] - prices[i-1]
        # 2、第i-1天持有股票，并休息，dp[i][1] = dp[i-1][1]
        # 【注意】prices的索引要比dp的索引快一天，即prices[i-1]指的是第i天的价格
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = 0 - prices[0] # 没有实际意义，为之后的循环逻辑正确而占位
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i-1][1] + prices[i-1] - fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i-1], dp[i-1][1])
        return dp[n][0]
        
# @lc code=end

