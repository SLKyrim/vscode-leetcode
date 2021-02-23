#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stocj-iv/description/
#
# algorithms
# Hard (29.55%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    19.8k
# Total Submissions: 66.8k
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfitII(self, prices: List[int]) -> int:
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
            dp[i][0] = max(dp[i-1][1] + prices[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i-1], dp[i-1][1])
        return dp[n][0]


    def maxProfit(self, k: int, prices: List[int]) -> int:
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
        if k > n // 2:
            # k超过天数一半时相当于买进次数无限制，避免k过大
            return self.maxProfitII(prices)

        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n+1)]
        for j in range(k+1):
            dp[0][j][1] = -prices[0]  # 没有实际意义，为之后的循环逻辑正确而占位
        for i in range(1, n + 1):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][1] + prices[i-1], dp[i-1][j][0])
                dp[i][j][1] = max(dp[i-1][j-1][0] - prices[i-1], dp[i-1][j][1])
        return dp[n][k][0]
# @lc code=end

