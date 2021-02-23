#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#
# https://leetcode-cn.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (49.96%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 11.3K
# Testcase Example:  '[4,14,2]'
#
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 
# 计算一个数组中，任意两个数之间汉明距离的总和。
# 
# 示例:
# 
# 
# 输入: 4, 14, 2
# 
# 输出: 6
# 
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
# 
# 
# 注意:
# 
# 
# 数组中元素的范围为从 0到 10^9。
# 数组的长度不超过 10^4。
# 
# 
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 字符串format格式化：https://www.runoob.com/python/att-string-format.html
        tmp = []
        for num in nums:
            tmp.append("{:0>32b}".format(num))
        res = 0
        # 星号将map中的元组拆分，如原来是(a,b,c)拆为a,b,c
        for bit in zip(*map(tuple, tmp)): 
            res += bit.count("1") * bit.count("0")
        return res
        
# @lc code=end

