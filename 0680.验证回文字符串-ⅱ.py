#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.47%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    44K
# Total Submissions: 111.6K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(ss):
            n = len(ss)
            left, right = 0, n-1
            while left < right:
                if ss[left] != ss[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if s[left] != s[right]:
                return helper(s[left:right]) or helper(s[left+1:right+1])
            left += 1
            right -= 1
        return True
            

        
# @lc code=end

