#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (65.16%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    71.1K
# Total Submissions: 108.4K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 
# 
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            # 因为是三角形，对第i层，有i+1个元素，最后一个元素的索引为i
            for j in range(1, i):
                # 对除了第1个和最后1个元素之外的元素遍历
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[-1])

        # DFS超时
        # def dfs(depth, cur, ind):
        #     if depth == len(triangle):
        #         self.res = min(self.res, cur)
        #         return
        #     dfs(depth+1, cur + triangle[depth+1-1][ind], ind)
        #     if ind + 1 < len(triangle[depth+1-1]):
        #         dfs(depth+1, cur+triangle[depth+1-1][ind+1], ind+1)
        
        # self.res = float("inf")
        # dfs(1, triangle[0][0], 0)
        # return self.res
# @lc code=end

