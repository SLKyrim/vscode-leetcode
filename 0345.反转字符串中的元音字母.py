#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (48.22%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 38.1K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        voweltmp = []
        for ch in s:
            if ch in vowel:
                voweltmp.append(ch)
        voweltmp = voweltmp[::-1]
        for i in range(len(s)):
            if s[i] in vowel:
                s = s[:i] + voweltmp.pop(0) + s[i+1:]
        return s
# @lc code=end

