#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (48.68%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 48.2K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            cur = n1 + n2 + carry
            carry = cur // 10
            res = str(cur % 10) + res
            i, j = i - 1, j - 1
        return str(carry) + res if carry else res 

        # 太长了
        # i, j = len(num1) - 1, len(num2) - 1
        # carry = 0
        # res = []
        # while i >= 0 and j >= 0:
        #     cur = int(num1[i]) + int(num2[j]) + carry
        #     carry = cur // 10
        #     res.insert(0, str(cur % 10))
        #     i -= 1
        #     j -= 1
        # if i < 0:
        #     while j >= 0:
        #         cur = int(num2[j]) + carry
        #         carry = cur // 10
        #         res.insert(0, str(cur % 10))
        #         j -= 1
        # else:
        #     while i >= 0:
        #         cur = int(num1[i]) + carry
        #         carry = cur // 10
        #         res.insert(0, str(cur % 10))
        #         i -= 1
        # if carry > 0:
        #     res.insert(0, str(carry))
        # return "".join(res)

# @lc code=end

