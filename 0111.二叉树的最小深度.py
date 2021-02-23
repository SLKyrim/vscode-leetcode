#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (40.78%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    56.3K
# Total Submissions: 135K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        # 非节点自然不算深度，顺便做递归结束条件
        if not root:
            return 0
        # 当前节点没有左右孩子，即叶节点，算一个深度，顺便做递归结束条件
        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 若当前节点有孩子且有一个孩子为空，当前节点非叶子节点，需要往孩子方向继续递归，空孩子深度为0，故两者相加即可
        if not root.left or not root.right:
            return left + right + 1
        # 当前节点有两个非空孩子，取较小深度并加上自己的1个深度
        return min(left, right) + 1
# @lc code=end

