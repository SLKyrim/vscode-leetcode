#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (57.18%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 29.9K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
# 
# 
# 
# 示例：
# 
# 输入：
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# 输出：
# 1
# 
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return float("inf")
        if not root.left and not root.right:
            return float("inf")
        left, right = float("inf"), float("inf")
        if root.left:
            node = root.left
            while node.right:
                node = node.right
            left = root.val - node.val
        if root.right:
            node = root.right
            while node.left:
                node = node.left
            right = node.val - root.val
        res = min(left, right)
        return min(res, self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))
        
# @lc code=end

