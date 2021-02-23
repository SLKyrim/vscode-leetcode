#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (38.82%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 41.3K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 
# 示例 1:
# 
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# 注意:
# 
# 
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        res = sum / k
        for i in range(k, len(nums)):
            sum -= nums[i-k]
            sum += nums[i]
            res = max(res, sum / k)
        return res        
        
# @lc code=end

