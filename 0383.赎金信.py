#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.66%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 25.3K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom)
# 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true
# ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
# 
# 注意：
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = set()
        for ch in ransomNote:
            tmp.add(ch)
        for ch in tmp:
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True
        
# @lc code=end

