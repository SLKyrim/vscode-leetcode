#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.58%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    28.9K
# Total Submissions: 77.5K
# Testcase Example:  '[2,3,2]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 思路：环形，则第一间和最后一间不可同时被偷
        # 分别对不包含第一间和不包含最后一间的房屋进行动态规划偷窃，最后取两者较大者
        # 这两间房都不偷的可能性已包含在以上两种情况中，故可不用重复计算
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp1 = [0] * (len(nums) - 1) # 不包含第一间
        dp2 = list()
        dp2[:] = dp1 # 不包含最后一间
        
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-2]+nums[i+1], dp1[i-1])
        
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])

        return max(dp1[-1], dp2[-1])

# @lc code=end

