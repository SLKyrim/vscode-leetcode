#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (51.05%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 27.6K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = [0 for i in range(128)]
        for c in s:
            cnt[ord(c)] += 1
        res = 0
        for num in cnt:
            res += num // 2 * 2
            if num % 2 == 1 and res % 2 == 0:
                res += 1
        return res  
# @lc code=end

