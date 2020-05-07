#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#
# https://leetcode-cn.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (37.80%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 19K
# Testcase Example:  '[1,1,2,2,2]'
#
# 
# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
# 
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
# 
# 示例 1:
# 
# 
# 输入: [1,1,2,2,2]
# 输出: true
# 
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 
# 
# 示例 2:
# 
# 
# 输入: [3,3,3,3,4]
# 输出: false
# 
# 解释: 不能用所有火柴拼成一个正方形。
# 
# 
# 注意:
# 
# 
# 给定的火柴长度和在 0 到 10^9之间。
# 火柴数组的长度不超过15。
# 
# 
#

# @lc code=start
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        perimeter = sum(nums)
        nums = sorted(nums)[::-1]
        line = perimeter // 4
        if perimeter % 4 != 0 or nums[0] > line or len(nums) < 4:
            return False

        lines = [0] * 4
        def dfs(ind):
            if ind == len(nums):
                if len(set(lines)) == 1:
                    return True
                return False

            for i in range(4):
                if lines[i] + nums[ind] > line:
                    continue
                lines[i] += nums[ind]
                if dfs(ind + 1):
                    return True
                lines[i] -= nums[ind]
            return False
        
        return dfs(0)
    
# @lc code=end

