#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (52.80%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 28.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False
        
        def dfs(node):
            res = 0
            if node.left:
                res = node.left.val if isLeaf(node.left) else dfs(node.left)
            if node.right:
                if not isLeaf(node.right):
                    res += dfs(node.right)
            return res

        return dfs(root)
        
# @lc code=end

