#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (47.15%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 26.8K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
# 
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
# 
# 
# 说明: 输入的数组长度最大不超过20,000.
# 
#

# @lc code=start
import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        tmp = collections.defaultdict(int)
        for num in nums:
            tmp[num] += 1
            if num - 1 in tmp:
                res = max(res, tmp[num-1] + tmp[num])
            if num + 1 in tmp:
                res = max(res, tmp[num+1] + tmp[num])
        return res   
# @lc code=end

