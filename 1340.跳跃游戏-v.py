#
# @lc app=leetcode.cn id=1340 lang=python3
#
# [1340] 跳跃游戏 V
#
# https://leetcode-cn.com/problems/jump-game-v/description/
#
# algorithms
# Hard (51.43%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 3.9K
# Testcase Example:  '[6,4,14,6,8,13,9,7,10,6,12]\n2'
#
# 给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：
# 
# 
# i + x ，其中 i + x < arr.length 且 0 < x <= d 。
# i - x ，其中 i - x >= 0 且 0 < x <= d 。
# 
# 
# 除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j
# 之间的数字（更正式的，min(i, j) < k < max(i, j)）。
# 
# 你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。
# 
# 请注意，任何时刻你都不能跳到数组的外面。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# 输出：4
# 解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。
# 注意，如果你从下标 6 开始，你只能跳到下标 7 处。你不能跳到下标 5 处因为 13 > 9 。你也不能跳到下标 4 处，因为下标 5 在下标 4 和
# 6 之间且 13 > 9 。
# 类似的，你不能从下标 3 处跳到下标 2 或者下标 1 处。
# 
# 
# 示例 2：
# 
# 输入：arr = [3,3,3,3,3], d = 3
# 输出：1
# 解释：你可以从任意下标处开始且你永远无法跳到任何其他坐标。
# 
# 
# 示例 3：
# 
# 输入：arr = [7,6,5,4,3,2,1], d = 1
# 输出：7
# 解释：从下标 0 处开始，你可以按照数值从大到小，访问所有的下标。
# 
# 
# 示例 4：
# 
# 输入：arr = [7,1,7,1,7,1], d = 2
# 输出：2
# 
# 
# 示例 5：
# 
# 输入：arr = [66], d = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5
# 1 <= d <= arr.length
# 
# 
#

# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # # 方法1：DFS+记忆化搜索 808ms
        # n = len(arr)

        # def dfs(i):
        #     if dp[i] != -1:
        #         # 剪枝：记忆化搜索
        #         return dp[i]
        #     res = 1
        #     # 向右搜索
        #     for j in range(i+1, i+d+1):
        #         if j < n and arr[j] < arr[i]:
        #             res = max(res, dfs(j) + 1)
        #         else:
        #             break
        #     # 向左搜索
        #     for j in range(i-1, i-d-1, -1):
        #         if j >= 0 and arr[j] < arr[i]:
        #             res = max(res, dfs(j) + 1)
        #         else:
        #             break
        #     dp[i] = res
        #     return res

        # dp = [-1 for _ in range(n)]
        # res = 0
        # for i in range(n):
        #     res = max(res, dfs(i))
        # return res


        # 以下四法均参考自：https://mp.weixin.qq.com/s/kEQ00_WLqDTG6tbsjQ2Xjw
        # # 方法1精简版：DFS+记忆化搜索 自顶向下DP O(nd) 876ms
        # n = len(arr)
        # dp = [0 for _ in range(n)]

        # def dfs(i):
        #     if dp[i]:
        #         return dp[i]
        #     dp[i] = 1
        #     for direction in [1, -1]:
        #         for j in range(i + direction, i + direction * (d+1), direction):
        #             if not (0 <= j < n and arr[j] < arr[i]):
        #                 break
        #             dp[i] = max(dp[i], dfs(j) + 1)
        #     return dp[i]

        # return max(map(dfs, range(n)))


        # # 方法2：自底向上递推DP O(nlogn+nd) 836ms
        # # 先求出高度低的台阶可达的台阶数，
        # # 然后从高的台阶跳1步到此低的台阶时，直接加上之前求出的台阶数即可
        # n = len(arr)
        # dp = [1 for _ in range(n)]
        # for height, i in sorted([height, i] for i, height in enumerate(arr)):
        #     # 按height排序，故height在前
        #     for direction in [1, -1]:
        #         for j in range(i + direction, i + direction * (d+1), direction):
        #             if not (0 <= j < n and arr[j] < arr[i]):
        #                 break
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)


        # 方法3：线段树+DP O(nlogn) 104ms
        # 没看懂
        n = len(arr)
        dp = [1 for _ in range(n+1)]
        stack = []
        arr.append(float("inf"))
        for i, height in enumerate(arr):
            while stack and arr[stack[-1]] < height:
                tmp = [stack.pop()]
                while stack and arr[stack[-1]] == arr[tmp[0]]:
                    tmp.append(stack.pop())
                for j in tmp:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])


        # # 方法4：单调栈+DP O(n) 136ms
        # # 没看懂
        # n = len(arr)
        # res = 0
        # dp = [1 for _ in range(n+1)]
        # stack, stack2 = [], []
        # arr.append(float("inf"))
        # for i in range(n+1):
        #     a = arr[i]
        #     while stack and arr[stack[-1]] < arr[i]:
        #         pre = arr[stack[-1]]
        #         while stack and pre == arr[stack[-1]]:
        #             j = stack.pop()
        #             if i - j <= d:
        #                 dp[i] = max(dp[i], dp[j] + 1)
        #             stack2.append(j)
        #         while stack2:
        #             j = stack2.pop()
        #             if stack and j - stack[-1] <= d:
        #                 dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
        #     stack.append(i)
        # return max(dp[:-1])

# @lc code=end

