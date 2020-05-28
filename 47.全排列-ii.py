
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (58.60%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 102.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # 状态回溯DFS
        def dfs(depth, path):
            if depth == len(nums):
                self.res.append(path[:])
                return
            
            for i in range(len(nums)):
                if not self.used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                        # 必须剪枝：被回溯到未使用状态且与当前节点同值的上一节点会被重复使用
                        continue
                    self.used[i] = True
                    path.append(nums[i])
                    dfs(depth+1, path)
                    self.used[i] = False
                    path.pop()

        nums.sort() # 排序后才能剪枝

        if not nums:
            return []

        self.res = []
        self.used = [False for _ in range(len(nums))]
        dfs(0, [])
        return self.res

        # 拼接数组DFS
        # # res = set() # list是可变类型，不是唯一的，即不是hashable的，不能放入set中
        # res = []

        # def dfs(cur, tmp):
        #     if not cur:
        #         if tmp not in res:
        #             res.append(tmp)
        #         return
        #     for i in range(len(cur)):
        #         dfs(cur[:i] + cur[i+1:], tmp + [cur[i]])

        # dfs(nums, [])
        # return list(res)
# @lc code=end

