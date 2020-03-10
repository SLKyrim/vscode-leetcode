#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.73%)
# Likes:    784
# Dislikes: 0
# Total Accepted:    139.8K
# Total Submissions: 264.7K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路：只能交易一次，因为这是个动态的过程，不能单纯找最小值买进，最大值卖出，因为可能会出现类似7-4 > 3-1的情况
        # 所以要在遍历过程中维护当前见过的最小值，并用当前价值减去见过的最小值来维护最大收益
        res = 0
        minp = float('inf') # 记录遍历过程中的最小价
        for price in prices:
            res = max(res, price - minp)
            minp = min(minp, price)
        return res
# @lc code=end

