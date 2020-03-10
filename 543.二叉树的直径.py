#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (46.38%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 48.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
# 
# 示例 :
# 给定二叉树
# 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 思路：最长直径不一定经过根节点
# 故转为求所有节点最大的左右子树深度和

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def maxDepth(node):
            if not node:
                return 0   
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        
        maxDepth(root)
        return self.res
# @lc code=end

