#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#
# https://leetcode-cn.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (20.76%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 19.8K
# Testcase Example:  '"172.16.254.1"'
#
# 编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。
# 
# IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
# 
# 同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。
# 
# IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,
# 2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0
# 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6
# address地址 (即，忽略 0 开头，忽略大小写)。
# 
# 然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334
# 是无效的 IPv6 地址。
# 
# 同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334
# 是无效的。
# 
# 说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。
# 
# 示例 1:
# 
# 
# 输入: "172.16.254.1"
# 
# 输出: "IPv4"
# 
# 解释: 这是一个有效的 IPv4 地址, 所以返回 "IPv4"。
# 
# 
# 示例 2:
# 
# 
# 输入: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# 
# 输出: "IPv6"
# 
# 解释: 这是一个有效的 IPv6 地址, 所以返回 "IPv6"。
# 
# 
# 示例 3:
# 
# 
# 输入: "256.256.256.256"
# 
# 输出: "Neither"
# 
# 解释: 这个地址既不是 IPv4 也不是 IPv6 地址。
# 
# 
#

# @lc code=start
import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        # 模式((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]\.)重复3次
        #  + 1次模式(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])
        matchIpv4 = re.match(r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])', IP)
        # 模式(([0-9a-fA-F]{1,4})\:)重复7次 + 1次模式([0-9a-fA-F]{1,4})
        matchIpv6 = re.match(r'(([0-9a-fA-F]{1,4})\:){7}([0-9a-fA-F]{1,4})', IP)
        if matchIpv4:
            # 只要从0开始的范围内能匹配上，match()就相当于会返回True，
            # 因此像”1.1.1.1.abcdefg“也会被判断为合法地址，
            # 因此需要进一步把有效部分的长度【span()[1] - span()[0]】与输入IP长度对比来判断地址是否合法
            if (matchIpv4.span()[1] - matchIpv4.span()[0]) == len(IP):
                return "IPv4"
            else:
                return "Neither"
        elif matchIpv6:
            if (matchIpv6.span()[1] - matchIpv6.span()[0]) == len(IP):
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"

        
# @lc code=end

