#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (44.33%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 30.7K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
# 
# 示例 1:
# 
# 
# 输入: "abab"
# 
# 输出: True
# 
# 解释: 可由子字符串 "ab" 重复两次构成。
# 
# 
# 示例 2:
# 
# 
# 输入: "aba"
# 
# 输出: False
# 
# 
# 示例 3:
# 
# 
# 输入: "abcabcabcabc"
# 
# 输出: True
# 
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
# 
# 
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            if len(s) % (i + 1) == 0:
                # 元串长度应是子串长度的整数倍
                tmp = s[:i+1]
                for j in range(i+1, len(s), len(tmp)):
                    if s[j:j+len(tmp)] != tmp:
                        break
                    if j == len(s) - len(tmp):
                        return True
        return False

# @lc code=end

