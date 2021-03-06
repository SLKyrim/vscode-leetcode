#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (33.15%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    12.5K
# Total Submissions: 37K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
# 
# 示例:
# 
# 输入: "Hello, my name is John"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
# @lc code=end

