#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.01%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 24.4K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 
# 示例 1：
# 
# 
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 
# 
# 
# 注意:
# 
# 
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 
# 
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        sums = sum(nums)
        each = sums // k
        nums = sorted(nums)[::-1]
        if each * k != sums or nums[0] > each or len(nums) < k:
            return False
        
        subs = [0] * k
        
        def dfs(ind):
            if ind == len(nums):
                if len(set(subs)) == 1:
                    return True
                return False
            for i in range(k):
                if subs[i] + nums[ind] > each:
                    continue
                subs[i] += nums[ind]
                if dfs(ind + 1):
                    return True
                subs[i] -= nums[ind]

        return dfs(0)
   
# @lc code=end

