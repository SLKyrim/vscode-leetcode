#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (60.88%)
# Likes:    481
# Dislikes: 0
# Total Accepted:    121K
# Total Submissions: 195.4K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = dict()
        for num in nums:
            try:
                tmp[num] += 1
            except:
                tmp[num] = 1
        res, cur = 0, 0
        for k,v in tmp.items():
            if v > cur:
                res = k
                cur = v
        return res

# @lc code=end

