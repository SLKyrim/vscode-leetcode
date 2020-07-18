#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (40.58%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    18.6K
# Total Submissions: 44.4K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 示例 1:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s2), len(s1)
        # dp[i][j]表示s1的前i个字母和s2的前j个字符是否可以交错成s3的前i+j个字母
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n+1):
            for j in range(m+1):
                pos = i + j - 1
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[pos])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[pos])
        return dp[n][m]
# @lc code=end

