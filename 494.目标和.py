#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (44.21%)
# Likes:    279
# Dislikes: 0
# Total Accepted:    29.5K
# Total Submissions: 66.5K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
# 
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 
# 示例 1:
# 
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
# 
# 
# 注意:
# 
# 
# 数组非空，且长度不会超过20。
# 初始的数组的和不会超过1000。
# 保证返回的最终结果能被32位整数存下。
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # # DFS超时
        # def dfs(cur, i):
        #     if i == n and cur == S:
        #         return 1
        #     if i == n:
        #         return 0
        #     res = 0
        #     res += dfs(cur + nums[i], i+1)
        #     res += dfs(cur - nums[i], i+1)
        #     return res

        # n = len(nums)
        # return dfs(0, 0)
        

        # DP
        n = len(nums)
        # dp[i][j]表示前i个数组成和值j的方案数
        dp = [[0] * (n+1) for _ in range(2000+1)]
        dp[0][0+1000] = 1
        for i in range(1, n+1):
            for j in range(-1000, 1000+1):
                if dp[i-1][j+1000] > 0:
                    dp[i][j+1000-nums[i-1]] += dp[i-1][j+1000]
                    dp[i][j+1000+nums[i-1]] += dp[i-1][j+1000]
        return dp[n][S+1000]
                

        
# @lc code=end

