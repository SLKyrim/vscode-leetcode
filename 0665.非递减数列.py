#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (22.35%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 97.2K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 
# 
# 示例 2:
# 
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 
# 
# 
# 
# 说明：
# 
# 
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
# 
# 
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        
        cnt = 0 # 记录修改次数，每次修改后都保证nums[i]与nums[i-1]是非递减的
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            cnt += 1

        for i in range(1, n-1):
            right = nums[i+1]
            if nums[i] > right:
                cnt += 1
                if cnt > 1:
                    return False
                left = nums[i-1]
                if left > right:
                    # 最优改法是把right变大，如3 4 1只能把1变大
                    nums[i+1] = nums[i] 
                else:
                    # 否则是把nums[i]变小，如1 4 3只能把4变小
                    nums[i] = left 
        return True

# @lc code=end

