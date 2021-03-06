#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (42.32%)
# Likes:    683
# Dislikes: 0
# Total Accepted:    88.9K
# Total Submissions: 203.6K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 基于下面动态规划的思路
        # 从状态转移方程可以看出，当前状态只与前两个状态有关，因此可以用pre, cur两个变量来表示前两个状态，降低空间复杂度
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, n):
            tmp = cur
            cur = max(pre + nums[i], cur)
            pre = tmp
        return cur

        # # dp[i] 在前i个房子偷到的最大金额
        # # 状态转移方程：dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        # return dp[-1]
# @lc code=end

