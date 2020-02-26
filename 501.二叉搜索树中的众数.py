#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (42.63%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 20.6K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 
# 假定 BST 有如下定义：
# 
# 
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 
# 
# 例如：
# 给定 BST [1,null,2,2],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 返回[2].
# 
# 提示：如果众数超过1个，不需考虑输出顺序
# 
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root: TreeNode) -> List[int]:
        
        tmp = list()

        def inorder(node):
            if not node:
                return
            
            if node.left:
                inorder(node.left)
            tmp.append(node.val)
            if node.right:
                inorder(node.right)
                   
        inorder(root) # 中序遍历BST得到升序数列

        # 一些特殊情况
        if len(set(tmp)) == len(tmp):
            return tmp

        curr = 1 # 记录当前连续数的数目
        maxCurr = 0 # 记录最大的连续数的数目即众数
        for i in range(1, len(tmp)):
            if tmp[i] == tmp[i - 1]:
                curr += 1
                if i == len(tmp) - 1 and curr > maxCurr:
                    maxCurr = curr
            else:
                if curr > maxCurr:
                    maxCurr = curr
                curr = 1

        res = list()
        curr = 1
        for i in range(1, len(tmp)):
            if tmp[i] == tmp[i - 1]:
                curr += 1
                if i == len(tmp) - 1 and curr == maxCurr:
                    res.append(tmp[i])
            else:
                if curr == maxCurr:
                    res.append(tmp[i - 1])
                curr = 1

        return res
  
# @lc code=end

