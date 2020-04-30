#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.38%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    53.9K
# Total Submissions: 87.9K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates or min(candidates) > target:
            return []
        
        self.res = []
        candidates.sort() # 排序以剪枝

        def dfs(cur, curSum, curInd):
            # if curInd == len(candidates) or curSum > target:
            #     return
            if curSum == target:
                self.res.append(cur)
                return
            for i in range(curInd, len(candidates)):
                if curSum + candidates[i] > target:
                    break # 由排序实现的剪枝
                if i > curInd and candidates[i] == candidates[i-1]:
                    continue # 避免相同数得到多个相同组合
                dfs(cur + [candidates[i]], curSum + candidates[i], i + 1) # i+1,避免重复使用某个数
        
        dfs([], 0, 0)
        return self.res

# @lc code=end

