#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
# https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (40.99%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.6K
# Testcase Example:  '[3,6,5,1,8]'
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 
# 示例 2：
# 
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        dp = [0] * 3
        
        for i in range(len(nums)):
            mod = nums[i] % 3

            # 前置状态：如mod = 1时，a = dp[2]，而dp[2] + nums[i] = dp[0]，故此时dp[2]是dp[0]的前置状态
            a = dp[(3 + 0 - mod) % 3] # 在当前mod下，dp[0]的前置状态
            b = dp[(3 + 1 - mod) % 3] # 在当前mod下，dp[1]的前置状态
            c = dp[(3 + 2 - mod) % 3] # 在当前mod下，dp[2]的前置状态

            if a > 0 or mod == 0:
                dp[0] = max(dp[0], a + nums[i])
            if b > 0 or mod == 1:
                dp[1] = max(dp[1], b + nums[i])
            if c > 0 or mod == 2:
                dp[2] = max(dp[2], c + nums[i])

        return dp[0]


        # 自解
        # # 是求数组中元素所能组成的和值中能被3整除的最大的那个和值
        # # dp[i] 为模3余i的数字和
        # # dp[0],dp[1],dp[2]是可以相互转换的，转移方程为:
        # # 若 nums[i] % 3 == 0, dp[i] + nums[i]后还是dp[i]
        # # 若 nums[i] % 3 == 1, dp[i] + nums[i]后是dp[(i + 1) % 3]
        # # 若 nums[i] % 3 == 2, dp[i] + nums[i]后是dp[(i + 2) % 3]
        # dp = [0] * 3
        # dp0, dp1, dp2 = 0,0,0

        # for i in range(len(nums)):
        #     mod = nums[i] % 3

        #     if mod == 0:
        #         dp0 = max(dp[0], dp[0] + nums[i])
        #         if dp[1] > 0:
        #             dp1 = max(dp[1], dp[1] + nums[i])
        #         if dp[2] > 0:
        #             dp2 = max(dp[2], dp[2] + nums[i])
        #     if mod == 1:
        #         if dp[2] > 0:
        #             dp0 = max(dp[0], dp[2] + nums[i])
        #         dp1 = max(dp[1], dp[0] + nums[i])
        #         if dp[1] > 0:
        #             dp2 = max(dp[2], dp[1] + nums[i])
        #     if mod == 2:
        #         if dp[1] > 0:
        #             dp0 = max(dp[0], dp[1] + nums[i])
        #         if dp[2] > 0:
        #             dp1 = max(dp[1], dp[2] + nums[i])
        #         dp2 = max(dp[2], dp[0] + nums[i])
            
        #     dp[0], dp[1], dp[2] = dp0, dp1, dp2

        # return dp[0]
        
# @lc code=end

