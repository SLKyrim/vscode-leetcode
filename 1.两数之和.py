#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (46.97%)
# Likes:    6809
# Dislikes: 0
# Total Accepted:    662.9K
# Total Submissions: 1.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target: int):
        res = []
        tmp = dict()
        for i in range(len(nums)):
            rst = target - nums[i]
            if rst in tmp: # O(1)
                res.append(tmp[rst])
                res.append(i)
                break
            tmp[nums[i]] = i
        return res

        # # index()的时间复杂度貌似是O(1)
        # res = []
        # ind = len(nums) - 1
        # while nums:
        #     cur = nums.pop()
        #     try:
        #         res.append(nums.index(target-cur))
        #         res.append(ind)
        #         break
        #     except:
        #         ind -= 1
        # return res
        
# @lc code=end

