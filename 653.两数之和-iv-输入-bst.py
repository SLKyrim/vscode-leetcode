#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (55.70%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 32.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 
# 案例 1:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# 输出: True
# 
# 
# 
# 
# 案例 2:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# 输出: False
# 
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
    def findTarget(self, root: TreeNode, k: int) -> bool:

        def helper(node):
            if not node:
                return []
            res = []
            if node.left:
                res += helper(node.left)
            res.append(node.val)
            if node.right:
                res += helper(node.right)
            return res

        a = helper(root)
        left, right = 0, len(a) - 1
        while left < right:
            if a[left] + a[right] == k:
                return True
            elif a[left] + a[right] < k:
                left += 1
            else:
                right -= 1
        return False
        
# @lc code=end

