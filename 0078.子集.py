#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.18%)
# Likes:    578
# Dislikes: 0
# Total Accepted:    91.2K
# Total Submissions: 118K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start = 0, tmp = []):
            if len(tmp) == depth:
                self.res.append(tmp[:])
                return
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                dfs(i+1, tmp) # 注意这里是i+1，保证数字不会被重复使用
                tmp.pop() # 回溯
        
        self.res = []
        for depth in range(len(nums)+1):
            dfs()

        return self.res                    
# @lc code=end

