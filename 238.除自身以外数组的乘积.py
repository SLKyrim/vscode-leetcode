#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (68.05%)
# Likes:    419
# Dislikes: 0
# Total Accepted:    43.6K
# Total Submissions: 63.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
# 
# 
# 
# 示例:
# 
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
# 
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        res = []
        for i in range(len(nums)):
            res.append(tmp)
            tmp = tmp * nums[i]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * tmp
            tmp = tmp * nums[i]
        return res
            
# @lc code=end

