#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (62.89%)
# Likes:    513
# Dislikes: 0
# Total Accepted:    139K
# Total Submissions: 221.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
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
        if not root:
            return []

        # DFS
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        res = []
        dfs(root, 0)
        return res


        # # 迭代
        # tmp = [root]
        # cnt = len(tmp)
        # res = []
        # level = 0
        # while tmp:
        #     res.append([])
        #     for i in range(cnt):
        #         node = tmp.pop(0)
        #         res[level].append(node.val)
        #         if node.left:
        #             tmp.append(node.left)
        #         if node.right:
        #             tmp.append(node.right)
        #     level += 1
        #     cnt = len(tmp)
        # return res
        
# @lc code=end

