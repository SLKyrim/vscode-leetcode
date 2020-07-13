#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (42.58%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 39K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 S 包含从1到 n
# 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
# 
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
# 
# 
# 注意:
# 
# 
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。
# 
# 
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        tmp = set()
        res = []
        for num in nums:
            if num not in tmp:
                tmp.add(num)
            else:
                res.append(num)
                break
        n = len(nums)
        csum = n * (1 + n) // 2
        nsum = sum(nums)
        res.append(res[0] + csum - nsum)
        return res
            
# @lc code=end

