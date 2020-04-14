#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (54.95%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 41.4K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
# 
# 示例 1:
# 
# 输入: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 
# 示例 2:
# 
# 输入: [3,4,5,1,3,null,1]
# 
#     3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 答案思路：每个节点可选择偷或者不偷两种状态，根据题目意思，相连节点不能一起偷
# 1、当前节点选择偷时，那么两个孩子节点就不能选择偷了
# 2、当前节点选择不偷时，两个孩子节点只需要拿最多的钱出来就行(两个孩子节点偷不偷没关系)
# 我们使用一个大小为2的数组来表示，索引0代表不偷，1代表偷
# 任何一个节点能偷到的最大钱的状态可以定义为
# 1、当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
# 2、当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))
    
    def helper(self, node):
        if not node:
            return [0, 0]
        res = [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        res[0] = max(left) + max(right)
        res[1] = left[0] + right[0] + node.val
        return res
               
# @lc code=end

