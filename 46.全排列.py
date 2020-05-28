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
        
        # 状态回溯DFS
        def dfs(depth, path):
            if depth == len(nums):
                self.res.append(path[:]) # 这里需要对path进行拷贝，否则会跟着顶层path的改变而改变，最后回溯到根节点时path为[]
                return
            
            for i in range(len(nums)):
                if not self.used[i]:
                    self.used[i] = True # 标记节点为已使用，之后的DFS就不能再使用它了
                    path.append(nums[i])

                    dfs(depth+1, path)
                    # 状态回溯
                    self.used[i] = False
                    path.pop()
        
        self.res = []
        self.used = [False for _ in range(len(nums))] # 记录节点使用状态
        dfs(0, [])
        return self.res

        
        # 拼接数组DFS
        # self.res = []

        # def dfs(cur, tmp):
        #     if not cur:
        #         self.res.append(tmp)
        #         return 
            
        #     for i in range(len(cur)):
        #         dfs(cur[:i] + cur[i+1:], tmp + [cur[i]])

        # dfs(nums, [])

        # return self.res

# @lc code=end

