#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (47.14%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    33K
# Total Submissions: 69.5K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        if n == 0:
            return False
        
        tmpSum = sum(nums)
        if tmpSum % 2 != 0:
            return False

        target = tmpSum // 2
        # dp[i][j]表示前i个数是否可以得到一个和值j
        dp = [[False] * (target+1) for _ in range(n+1)]
        # 边界初始化
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, target+1):
            dp[0][i] = False
        # 状态转移
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j] # 避免进不了下面的条件
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                if dp[i][target] == True:
                    return True # 剪枝
        return dp[n][target]
        
# @lc code=end

