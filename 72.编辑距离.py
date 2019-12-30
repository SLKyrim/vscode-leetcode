#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (55.02%)
# Likes:    449
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 41.2K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 示例 1:
# 
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2:
# 
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 第一个单词前i个字母与第二个单词前j个字母的编辑距离
        len1, len2 = len(word1), len(word2)
        dp = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for i in range(len2 + 1):
            dp[0][i] = i
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
 
# @lc code=end

