#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#
# https://leetcode-cn.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (62.26%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 16.8K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
# 
# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
# 
# 
# 
# 示例：
# 
# 输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。
# 
# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= costs.length <= 100
# costs.length 为偶数
# 1 <= costs[i][0], costs[i][1] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = []
        for i in range(n):
            diff.append(costs[i][0] - costs[i][1])
        diff.sort()
        res = 0
        for i in range(n):
            if i < n // 2:
                res += diff[i]
            res += costs[i][1]
        return res

# @lc code=end

