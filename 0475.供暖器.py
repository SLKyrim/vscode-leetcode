
#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (28.76%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 24.8K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
# 
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
# 
# 说明:
# 
# 
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
# 
# 
# 示例 1:
# 
# 
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 
# 
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            # 得出的 left 所指的加热器并不一定是离房屋 house 最近的一个，需要判断以下情况
            if heaters[left] == house:
                # 若找到的值等于 house ，则说明 house 房屋处放有一个加热器，house 房屋到加热器的最短距离为 0
                continue
            elif heaters[left] < house:
                # 若该加热器的坐标值小于 house ，说明该加热器的坐标与 house 之间没有别的加热器
                res = max(res, house - heaters[left])
            elif left == 0:
                # 若left == 0 即二分查找的结果指向第一个加热器的坐标,说明 heaters[left] 坐标的房屋之前的位置未放置加热器,直接相减就是到房屋 house 最近加热器的距离
                res = max(res, heaters[left] - house)
            else:
                # 若left不等于 0 ，说明 house 介于left和left-1之间，房屋到加热器的最短距离就是left和left - 1处加热器与 house 差值的最小值.
                res = max(res, min(heaters[left] - house, house - heaters[left-1]))
        return res
 
# @lc code=end

