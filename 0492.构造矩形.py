#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#
# https://leetcode-cn.com/problems/construct-the-rectangle/description/
#
# algorithms
# Easy (49.67%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 14.5K
# Testcase Example:  '1'
#
# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W
# 且满足以下要求的矩形的页面。要求：
# 
# 
# 1. 你设计的矩形页面必须等于给定的目标面积。
# 
# 2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
# 
# 3. 长度 L 和宽度 W 之间的差距应当尽可能小。
# 
# 
# 你需要按顺序输出你设计的页面的长度 L 和宽度 W。
# 
# 示例：
# 
# 
# 输入: 4
# 输出: [2, 2]
# 解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
# 但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
# 
# 
# 说明:
# 
# 
# 给定的面积不大于 10,000,000 且为正整数。
# 你设计的页面的长度和宽度必须都是正整数。
# 
# 
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 以面积平方根为起点往下找，找到的第一个满足整除的点即为所求
        res = list()
        start = int(area**0.5)
        for i in range(start, 0, -1):
            if area % i == 0:
                res.append(max(i, area // i)) # 较大的长度放在前面
                res.append(min(i, area // i))
                break
        return res
        
# @lc code=end

