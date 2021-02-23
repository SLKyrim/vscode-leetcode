#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
# https://leetcode-cn.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (41.75%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 25.5K
# Testcase Example:  '[1,2,3]\n4'
#
# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
# 
# 示例:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# 请注意，顺序不同的序列被视作不同的组合。
# 
# 因此输出为 7。
# 
# 
# 进阶：
# 如果给定的数组中含有负数会怎么样？
# 问题会产生什么变化？
# 我们需要在题目中添加什么限制来允许负数的出现？
# 
# 致谢：
# 特别感谢 @pbrother 添加此问题并创建所有测试用例。
# 
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        
        # 动态规划
        if not nums or min(nums) > target:
            return 0
        # dp[i] 组合总和为i时，nums中的数所能组成的组合数的个数
        dp = [0] * (target + 1) 
        dp[0] = 1 # 和为0的组合数只有一个，即空集
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
        

        # DFS+回溯，超时（7/17）
        # if not nums or min(nums) > target:
        #     return 0

        # self.res = []
        # nums.sort()  # 排序以剪枝

        # self.tmp = []
        # def bk(cur, sub): # 回溯求全排列（LeetCode 47）
        #     if not sub:
        #         if cur not in self.tmp:
        #             self.tmp.append(cur)
        #         return
        #     for i in range(len(sub)):
        #         bk(cur + [sub[i]], sub[:i] + sub[i+1:])

        # def dfs(cur, curSum, curInd):
        #     if curSum == target:
        #         if len(set(cur)) == 1:
        #             self.res.append(cur)
        #         else:
        #             bk([], cur) # 回溯求全排列
        #             for ans in self.tmp:
        #                 self.res.append(ans)
        #             self.tmp = []
        #         return
        #     for i in range(curInd, len(nums)):
        #         if curSum + nums[i] > target:
        #             break  # 由排序实现的剪枝
        #         if i > curInd and nums[i] == nums[i - 1]:
        #             continue  # 避免相同数得到多个相同组合
        #         dfs(cur + [nums[i]], curSum + nums[i], i)
        
        # dfs([], 0, 0)
        # return len(self.res)

        
        # DFS+数学（排列组合） 超时 (12/17) 
        # if not nums or min(nums) > target:
        #     return 0

        # self.res = []
        # nums.sort()  # 排序以剪枝

        # def dfs(cur, curSum, curInd):
        #     if curSum == target:
        #         self.res.append(cur)
        #         return
        #     for i in range(curInd, len(nums)):
        #         if curSum + nums[i] > target:
        #             break  # 由排序实现的剪枝
        #         if i > curInd and nums[i] == nums[i - 1]:
        #             continue  # 避免相同数得到多个相同组合
        #         dfs(cur + [nums[i]], curSum + nums[i], i)

        # dfs([], 0, 0)

        # def fac(num):
        #     """求阶乘"""
        #     if num == 1 or num == 0:
        #         return 1
        #     return num * fac(num - 1)

        # def A(n, m):
        #     """求排列数"""
        #     return fac(n) // fac(n - m)

        # def C(n, m):
        #     """求组合数"""
        #     return fac(n) // (fac(m) * fac(n - m))

        # res = 0
        # for comb in self.res:
        #     n = len(comb)
        #     m = len(set(comb))
        #     if m == 1:
        #         res += 1
        #     elif n == m:
        #         res += A(n, m)
        #     else:
        #         # 有重复数的情况
        #         cnts = []
        #         for num in set(comb):
        #             cnts.append(comb.count(num))
        #         c1 = 0  # 记录个数为1的数的个数
        #         cm = [] # 记录个数大于1的数的个数
        #         cn = [] # 记录安排好cm后剩余的位置数
        #         ret = n # 记录剩余的位置
        #         for cnt in cnts:
        #             if cnt == 1:
        #                 c1 += 1
        #             else:
        #                 cn.append(ret)
        #                 cm.append(cnt)
        #                 ret -= cnt
        #         tmp = A(ret, c1) # 在安排完个数大于1的数后剩余的位置中安排个数为1的数的排列数
        #         for n, m in zip(cn, cm):
        #             tmp *= C(n, m) # 在n个位置中安排m个重复数的组合数
        #         res += tmp

        # return res
        
# @lc code=end

