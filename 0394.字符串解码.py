#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode-cn.com/problems/decode-string/description/
#
# algorithms
# Medium (50.02%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    30.9K
# Total Submissions: 60.8K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# 
# 示例:
# 
# 
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
# 
# 
#

# @lc code=start

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isdigit() or s[i].isalpha() or s[i] == "[":
                stack.append(s[i])
            else:
                # 碰到"]"时开始对之前入栈的字符出栈
                tmp = []
                while stack[-1] != "[":
                    tmp.append(stack.pop()) # 将[]内的字符串出栈
                tmp.reverse()
                cur = "".join(tmp)
                stack.pop() # 把"["出栈
                tmp = []
                while stack and stack[-1].isdigit():
                    tmp.append(stack.pop()) # 将[]前的数字出栈
                tmp.reverse()
                cnt = int("".join(tmp))
                while cnt > 0:
                    cnt -= 1
                    stack.append(cur) # 将[]内的字符串按[]前的数字表示的重复次数入栈
        return "".join(stack)


# 正则表达式解法
# import re

# class Solution:
#     def decodeString(self, s: str) -> str:
#         pattern = r"(\d+)\[(\w+)\]"
#         tmp = re.search(pattern, s)
#         while tmp:
#             l, r = tmp.span()[0], tmp.span()[1]
#             cur = s[l:r]
#             mid = cur.find("[")
#             num = int(cur[:mid])
#             chs = cur[mid + 1:-1] * num
#             s = s[:l] + chs + s[r:]
#             tmp = re.search(pattern, s)
#         return s

# @lc code=end


