#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (34.01%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 16.1K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
# 
# 示例 1:
# 
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]] 
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 示例 2:
# 
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]] 
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
# 
#

# @lc code=start
class Solution:
    def palindromePairs(self, words):

        def findWord(s: str, left: int, right: int) -> int:
            # 在哈希表中找s的子串s[left:right+1]，返回其在words中的索引，找不到返回-1
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            # 判断s的子串s[left:right+1]是否是回文
            sub = s[left:right+1]
            return sub == sub[::-1]

        n = len(words)
        # 哈希表，键为字串，值为字串在words中的索引
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    # 如果word的右子串word[j:m]为回文
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        # 如果word的左子串word[0:j]在哈希表中可索引，则为一种答案
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    # 如果word的左子串word[0:j]为回文
                    # 因为j=0的情况已在判断右子串是否回文中讨论过，为避免重复这里j不可等于0
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        # 如果word的右子串word[j:m]在哈希表中可索引，则为一种答案
                        ret.append([rightId, i])
        return ret
        
# @lc code=end

