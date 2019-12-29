# -*- coding: utf-8 -*-
"""
Created on 2019/12/27 17:07



Author: Long
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 到第i行第j列的路径数
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,2))