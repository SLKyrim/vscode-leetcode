#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (37.27%)
# Likes:    456
# Dislikes: 0
# Total Accepted:    58K
# Total Submissions: 152.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # ind = 0 # nums的索引位置
        # pre = 0 # 记录上次的最右边界
        # cur = 0 # 记录当前的右边界
        # res = True
        # while (ind < len(nums)):
        #     while ind < len(nums) and ind <= pre:
        #         # 在上次最右边界左边中的点找可以跳到更远位置的位置
        #         cur = max(cur, nums[ind] + ind)
        #         ind += 1
        #     pre = cur # 已当前能到达的最右边界更新pre供下一次循环使用
        #     if ind >= len(nums) or cur >= len(nums) - 1:
        #         break
        #     if cur < ind:
        #         # 现在的最右边界无法到达下一个ind索引位置
        #         res = False
        #         break
        # if cur < len(nums) - 1:
        #     res = False
        # return res


        # 尝试最远距离内的跳跃，并更新能跳到最远的距离
        right = 0
        for i in range(len(nums)):
            if i > right:
                return False
            right = max(right, i + nums[i])
        return True


        # # BFS 超时
        # n = len(nums)
        # visited = [0 for _ in range(n)]
        # visited[0] = 1
        # tmp = [0]
        # while tmp:
        #     cur = tmp.pop(0)
        #     if cur == n - 1:
        #         return True
        #     for v in range(cur, cur + nums[cur] + 1):
        #         if 0 <= v < n and visited[v] == 0:
        #             visited[v] = 1
        #             if v == n - 1:
        #                 return True
        #             tmp.append(v)
        # return False


# @lc code=end

