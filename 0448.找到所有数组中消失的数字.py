#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (54.78%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 47.9K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
# 
# 示例:
# 
# 
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
# 
# 
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = [False for i in range(len(nums))]
        res = []
        for num in nums:
            tmp[num - 1] = True
        for i in range(len(tmp)):
            if tmp[i] == False:
                res.append(i + 1)
        return res
        
# @lc code=end

