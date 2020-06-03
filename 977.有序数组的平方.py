#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (70.97%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    31.1K
# Total Submissions: 43.8K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
# 
# 
# 
# 示例 1：
# 
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 
# 
# 示例 2：
# 
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        right = 0 # 对正数的指针
        n = len(A)
        while right < n and A[right] < 0:
            right += 1
        left = right - 1 # 对负数的指针
        res = []
        while left >= 0 and right < n:
            n1, n2 = A[left]*A[left], A[right]*A[right]
            if n1 < n2:
                res.append(n1)
                left -= 1
            else:
                res.append(n2)
                right += 1
        
        while left >= 0:
            res.append(A[left]*A[left])
            left -= 1
        while right < n:
            res.append(A[right]*A[right])
            right += 1
        
        return res
        
# @lc code=end

