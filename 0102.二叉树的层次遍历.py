#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.05%)
# Likes:    401
# Dislikes: 0
# Total Accepted:    86.7K
# Total Submissions: 141.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # 迭代：用先进先出队列保存节点，记录每层节点数，每个循环更新该数
        if not root:
            return []

        res = list()
        queue = [root]
        level = len(queue) # 记录当前层的节点数

        while queue:
            tmp = list() # 记录每层的res
            for i in range(level):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
            level = len(queue)
        return res

        ### 递归
        # if not root:
        #     return []
        # res = list()

        # def dfs(node, level):
        #     if len(res) == level:
        #         res.append([])
        #     res[level].append(node.val)
        #     if node.left:
        #         dfs(node.left, level + 1)
        #     if node.right:
        #         dfs(node.right, level + 1)
        
        # dfs(root, 0)
        # return res

# @lc code=end

