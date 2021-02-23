#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (69.25%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    55.8K
# Total Submissions: 79.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root):
        
        # ### 取巧迭代：先压左孩子，再压右孩子（和前序迭代遍历相反），最后逆序输出
        # if not root:
        #     return []
        # res = list()
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return res[::-1]
        

        ### 迭代：若未访问过当前节点的左右孩子，则先压右孩子，再压左孩子
        # 若当前的左右孩子都访问过了，才访问当前节点并将其弹出栈
        # 需要用一个集合保存访问过的节点
        if not root:
            return []

        res = list()
        visNode = set() # 记录访问过得节点
        stack = [root]
        while stack:
            node = stack[-1]
            isVisLeft = True # 是否访问过左孩子的标记
            isVisRight = True # 是否访问过右孩子的标记
            if node.right and node.right not in visNode:
                isVisRight = False
                stack.append(node.right)
            if node.left and node.left not in visNode:
                isVisLeft = False
                stack.append(node.left)
            if isVisLeft and isVisRight:
                res.append(node.val) # 当前节点左右孩子都访问过了才将该节点的值放进res
                stack.pop()
                visNode.add(node)
        return res

        ### 递归
        # if not root:
        #     return []
        # res = list()
        # if root.left:
        #     res += self.postorderTraversal(root.left)
        # if root.right:
        #     res += self.postorderTraversal(root.right)
        # res += [root.val]
        # return res
# @lc code=end

