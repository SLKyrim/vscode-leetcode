#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#
# https://leetcode-cn.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (60.60%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 24.1K
# Testcase Example:  '5'
#
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
# 
# 示例 1:
# 
# 
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
# 
# 
# 示例 2:
# 
# 
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
# 
# 
# 示例 3:
# 
# 
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
# 
# 
# 示例 4:
# 
# 
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
# 
# 
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)[2:]
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                return False
        return True
   
# @lc code=end

