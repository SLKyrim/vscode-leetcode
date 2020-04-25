#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (73.22%)
# Likes:    621
# Dislikes: 0
# Total Accepted:    104.9K
# Total Submissions: 140.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        self.res = []

        def dfs(cur, tmp):
            if not cur:
                self.res.append(tmp)
                return 
            
            for i in range(len(cur)):
                dfs(cur[:i] + cur[i+1:], tmp + [cur[i]])

        dfs(nums, [])

        return self.res
# @lc code=end

