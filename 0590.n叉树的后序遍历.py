#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (71.16%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 23.7K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其后序遍历: [5,6,3,2,4,1].
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        # 取巧迭代：(逆前序再逆序即后序)从左向右将当前节点压入栈，最后输出结果逆序
        if not root:
            return []
        res = list()
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]

        # 迭代：超时
        # if not root:
        #     return []
        # res = list()
        # visNode = set()
        # stack = [root]
        # while stack:
        #     node = stack[-1]
        #     childNum = len(node.children)
        #     visited = [True for i in range(childNum)]
        #     for i in range(childNum - 1, -1, -1):
        #         child = node.children[i]
        #         if child not in visNode:
        #             visited[i] = False
        #             stack.append(child)
        #     if len(set(visited)) == 1:
        #         stack.pop()
        #         res.append(node.val)
        #         visNode.add(node)
        # return res

        ### 递归
        # if not root:
        #     return []
        # res = list()
        # for child in root.children:
        #     res += self.postorder(child)
        # res += [root.val]
        # return res
        
# @lc code=end

