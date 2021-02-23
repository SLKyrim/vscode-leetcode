#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (69.31%)
# Likes:    409
# Dislikes: 0
# Total Accepted:    111K
# Total Submissions: 157.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ### 迭代 先全压左孩子，再压这些左孩子的右孩子
        if not root:
            return []
        
        res = list()
        stack = list()
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

        ### 递归
        # if not root:
        #     return []
        # res = list()
        # if root.left:
        #     res += self.inorderTraversal(root.left)
        # res += [root.val]
        # if root.right:
        #     res += self.inorderTraversal(root.right)
        # return res
# @lc code=end

