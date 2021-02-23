#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (70.98%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 27.1K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.res = []
        nums = range(1, 10)

        def dfs(cur, curSum, curCnt, curInd):
            if curSum == n and curCnt == k:
                self.res.append(cur)
                return
            if curCnt == k and curInd == 10:
                return
            for i in range(curInd, 10):
                if curSum + i > n:
                    break # 1->9升序实现的剪枝
                dfs(cur + [i], curSum + i, curCnt + 1, i + 1)

        dfs([], 0, 0, 1)
        return self.res

# @lc code=end

