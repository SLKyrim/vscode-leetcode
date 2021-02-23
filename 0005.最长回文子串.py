#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.90%)
# Likes:    1816
# Dislikes: 0
# Total Accepted:    196.3K
# Total Submissions: 682.5K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expend(s, i, i)  # 奇数长度的回文串长度
            len2 = self.expend(s, i, i + 1)  # 偶数长度的回文串长度
            if len1 > len2:
                if len1 > end - start:
                    start = i - len1 // 2
                    end = i + len1 // 2
            else:
                if len2 > end - start:
                    start = i - (len2 - 1) // 2
                    end = i + (len2 - 1) // 2 + 1
        return s[start:end+1]

    def expend(self, s, l, r):
        left, right = l, r
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1
# @lc code=end

