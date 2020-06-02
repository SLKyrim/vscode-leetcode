#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#
# https://leetcode-cn.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (31.17%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 6.8K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
# 
# 每一步，你可以从下标 i 跳到下标：
# 
# 
# i + 1 满足：i + 1 < arr.length
# i - 1 满足：i - 1 >= 0
# j 满足：arr[i] == arr[j] 且 i != j
# 
# 
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
# 
# 注意：任何时候你都不能跳到数组外面。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
# 
# 
# 示例 2：
# 
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
# 
# 
# 示例 3：
# 
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
# 
# 
# 示例 4：
# 
# 输入：arr = [6,1,9]
# 输出：2
# 
# 
# 示例 5：
# 
# 输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
# 
# 
#

# @lc code=start
import collections

class Solution:
    def minJumps(self, arr) -> int:
        # # 尝试DFS失败
        # def dfs(cur, step):
        #     if cur == n - 1:
        #         return step
        #     res = float('inf')
        #     for v in hashMap[arr[cur]] + [cur - 1, cur + 1]:
        #         if 0 <= v < n and visited[v] == 0:
        #             visited[v] = 1
        #             res = min(res, dfs(v, step + 1))
        #     hashMap[arr[cur]] = []  # 剪枝：防止对同值索引的重复搜索
        #     return res

        # n = len(arr)
        # hashMap = collections.defaultdict(list)  # 键为数组中的数值，值为拥有这些数值的索引
        # for i in range(n):
        #     hashMap[arr[i]].append(i)
        # visited = [0 for _ in range(n)]
        # visited[0] = 1
        # return dfs(0, 0)
            
        
        # BFS
        n = len(arr)
        hashMap = collections.defaultdict(list) # 键为数组中的数值，值为拥有这些数值的索引
        for i in range(n):
            hashMap[arr[i]].append(i)
        tmp = [0]
        visited = [0 for _ in range(n)]
        visited[0] = 1
        res = 0
        while tmp:
            now = len(tmp)
            for i in range(now):
                cur = tmp.pop(0)
                if cur == n - 1:
                    return res
                nex = hashMap[arr[cur]]
                nex += [cur - 1, cur + 1]
                for v in nex:
                    if 0 <= v < n and visited[v] == 0:
                        visited[v] = 1
                        tmp.append(v)
                hashMap[arr[cur]] = [] # 剪枝：防止对同值索引的重复搜索
            res += 1
        return res

# @lc code=end

