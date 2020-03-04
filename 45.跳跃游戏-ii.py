#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (32.38%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 96.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 示例:
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 说明:
# 
# 假设你总是可以到达数组的最后一个位置。
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        ind = 0 # nums的索引位置
        pre = 0 # 记录上次的最右边界
        cur = 0 # 记录当前的右边界
        res = 0
        while (ind < len(nums)):
            while ind < len(nums) and ind <= pre:
                # 在上次最右边界左边中的点找可以跳到更远位置的位置
                cur = max(cur, nums[ind] + ind)
                ind += 1
            pre = cur # 已当前能到达的最右边界更新pre供下一次循环使用
            res += 1
            if ind >= len(nums) or cur >= len(nums) - 1:
                break
            if cur < ind:
                # 现在的最右边界无法到达下一个ind索引位置
                res = -1
                break
        if cur < len(nums) - 1:
            res = -1
        return res
# @lc code=end

