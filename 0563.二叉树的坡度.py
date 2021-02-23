#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#
# https://leetcode-cn.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (55.44%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    13.7K
# Total Submissions: 24.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，计算整个树的坡度。
# 
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
# 
# 整个树的坡度就是其所有节点的坡度之和。
# 
# 
# 
# 示例：
# 
# 输入：
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# 输出：1
# 解释：
# 结点 2 的坡度: 0
# 结点 3 的坡度: 0
# 结点 1 的坡度: |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 
# 
# 
# 
# 提示：
# 
# 
# 任何子树的结点的和不会超过 32 位整数的范围。
# 坡度的值不会超过 32 位整数的范围。
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
    def findTilt(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            self.res += abs(left - right)
            node.val += left + right
            return node.val

        self.res = 0
        dfs(root)
        return self.res
        
# @lc code=end

