#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (61.28%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 5.6K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 返回与给定的前序和后序遍历匹配的任何二叉树。
# 
# pre 和 post 遍历中的值是不同的正整数。
# 
# 
# 
# 示例：
# 
# 输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
# 每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
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
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        leftRoot = pre[1]
        leftRootInd = post.index(leftRoot)
        postLeft = post[:leftRootInd+1]
        postRight = post[leftRootInd+1:-1]
        preLeft = pre[1:1+len(postLeft)]
        preRight = pre[1+len(postLeft):]
        root = TreeNode(pre[0])
        root.left = self.constructFromPrePost(preLeft, postLeft)
        root.right = self.constructFromPrePost(preRight, postRight)
        return root
 
# @lc code=end

