#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (42.55%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 232.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # res = []
        # new = sorted(intervals, key=lambda x:x[0])
        # left, right = float("-inf"), float("-inf")
        # for inter in new:
        #     if inter[0] > right:
        #         res.append([left, right])
        #         left = inter[0]
        #         right = inter[1]
        #     if inter[0] <= right and inter[1] > right:
        #         right = inter[1]
        # res.append([left, right])
        # res.pop(0)
        # return res

        res = []
        intervals.sort(key=lambda x:x[0])
        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter) # 新的与之前的区间不重合的区间
            else:
                res[-1][1] = max(res[-1][1], inter[1]) # 更新右边界
        return res

# @lc code=end

