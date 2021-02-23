#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.28%)
# Likes:    1916
# Dislikes: 0
# Total Accepted:    125.1K
# Total Submissions: 343.5K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        length = m + n
        left, right = -1, -1
        aStart, bStart = 0, 0
        for i in range(length // 2 + 1):
            left = right
            if aStart < m and (bStart >= n or nums1[aStart] < nums2[bStart]):
                right = nums1[aStart]
                aStart += 1
            else:
                right = nums2[bStart]
                bStart += 1
        if length & 1 == 0:
            return (left + right) / 2
        else:
            return right

# @lc code=end

