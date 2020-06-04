#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (38.14%)
# Likes:    607
# Dislikes: 0
# Total Accepted:    72.3K
# Total Submissions: 182.4K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # 正常思路DP，O(n^2)超时
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)] # dp[i][j]表示[i,j]区间的最大值
        # res = float("-inf")
        # for i in range(n):
        #     dp[i][i] = nums[i]
        #     res = max(res, nums[i])
        # for i in range(n):
        #     for j in range(i+1, n):
        #         dp[i][j] = dp[i][j-1] * nums[j]
        #         res = max(res, dp[i][j])
        # return res
        
        # DP, O(n)
        n = len(nums)
        dpMax = nums[:] # dpMax[i]表示以i结尾的子数组最大乘积
        dpMin = nums[:] # dpMin[i]表示以i结尾的子数组最小乘积
        for i in range(1, n):
            dpMax[i] = max(dpMax[i-1]*nums[i], dpMin[i-1]*nums[i], nums[i])
            dpMin[i] = min(dpMax[i-1]*nums[i], dpMin[i-1]*nums[i], nums[i])
        return max(dpMax)

# @lc code=end

