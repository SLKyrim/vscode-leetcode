#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (63.72%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    46.9K
# Total Submissions: 73.5K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 层序遍历，取每层最右边的
        if not root:
            return []
        queue = [root]
        curL = len(queue)
        res = []
        while queue:
            for i in range(curL):
                node = queue.pop(0)
                if i == curL - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            curL = len(queue)
        return res


        # DFS list trick
        # self.res = []

        # def dfs(node, depth):
        #     if not node:
        #         return
        #     if depth == len(self.res):
        #         # 当前深度的最右节点
        #         self.res.append(node.val)
        #     dfs(node.right, depth + 1) # 先DFS右边
        #     dfs(node.left, depth + 1)

        # dfs(root, 0)
        # return self.res

# @lc code=end

