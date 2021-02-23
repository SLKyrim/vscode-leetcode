#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (50.29%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    21.6K
# Total Submissions: 42.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 
# 示例 1:
# 
# 
# 输入: [1,2,3]
# 输出: 6
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: 24
# 
# 
# 注意:
# 
# 
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
# 
# 
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 一次遍历找最小的两个数和最大的三个数 O(n)
        min1, min2 = 1001, 1001
        max1, max2, max3 = -1001, -1001, -1001
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)

        # 排序 O(nlogn)
        # nums.sort()
        # left, right = 0, 0
        # if nums[0] < 0 and nums[1] < 0:
        #     left = nums[0] * nums[1] * nums[-1]
        # right = nums[-2] * nums[-1] * nums[-3]
        # return max(left, right)   
        
# @lc code=end

