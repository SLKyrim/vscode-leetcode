#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (32.52%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 44.6K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
# 
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 
# 
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 
# 
# 仅当你可选的 X >= 2 时返回 true。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 
# 
# 示例 2：
# 
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 3：
# 
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 4：
# 
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 
# 
# 示例 5：
# 
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
# 
# 
# 
# 提示：
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cards = set(deck)
        cnts = list()
        for card in cards:
            cnts.append(deck.count(card))
        
        # 求数组的最大公约数
        for i in range(min(cnts), 0, -1):
            if list(filter(lambda x: x % i != 0, cnts)) == []:
                if i >= 2:
                    return True
        return False

# @lc code=end

