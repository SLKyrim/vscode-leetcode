#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (46.82%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 28.3K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 示例 1:
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2:
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
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

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        def helper(node):
            res = [node.val]
            if node.left:
                res += helper(node.left)
            if node.right:
                res += helper(node.right)
            return res

        a = set(helper(root))
        min1, min2 = float("inf"), float("inf")
        for num in a:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return min2 if min2 != float("inf") else -1

# @lc code=end

