#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (51.33%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    13.7K
# Total Submissions: 26.5K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 完全背包DP
        n = len(coins)
        # dp[i][j]表示前i种硬币凑成总金额j的组合数
        dp = [[0] * (amount+1) for _ in range(n+1)]
        # 初始化
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j - coins[i-1] >= 0:
                    # 如果是01背包，那么
                    # dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i-1]]
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[n][amount]
        
        
        # 空间优化DP
        # dp = [0] * (amount + 1) # dp[i]表示凑金额i的组合数
        # dp[0] = 1
        # # # 这里求的是排列数，题目求的是组合数，注意区分
        # # for i in range(amount + 1):
        # #     for coin in coins:
        # #         if i - coin >= 0:
        # #             dp[i] += dp[i - coin]
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] += dp[i - coin]
        # return dp[amount]

        
# @lc code=end

