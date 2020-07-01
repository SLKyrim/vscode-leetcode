#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (50.28%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 49.5K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 示例 1:
# 
# 
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释: 
# 长度最长的公共子数组是 [3, 2, 1]。
# 
# 
# 说明:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # dp[i][j]表示A[i:]和B[j:]的最长前缀长度
        # if A[i] == B[j]：dp[i][j] = dp[i+1][j+1] + 1 else dp[i][j] = 0
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    res = max(res, dp[i][j])
        return res
# @lc code=end

