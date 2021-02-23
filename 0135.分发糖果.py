#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode-cn.com/problems/candy/description/
#
# algorithms
# Hard (40.65%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 36.6K
# Testcase Example:  '[1,0,2]'
#
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
# 
# 
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 
# 
# 那么这样下来，老师至少需要准备多少颗糖果呢？
# 
# 示例 1:
# 
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 
# 
# 示例 2:
# 
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
# 
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for i in range(len(ratings))]
        right = left[:] # 相当于left.copy()
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        res = 0
        for i in range(len(ratings)):
            res += max(left[i], right[i])
        return res
# @lc code=end

