#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (58.27%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    61.4K
# Total Submissions: 102.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # pre 为了将当前反转部分与已反转部分相连
        # end 为了确定每次反转部分的末尾
        pre, end = dummy, dummy 

        def reverse(node):
            pre = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp 
            return pre

        while end.next:
            i = 0
            while i < k and end:
                end = end.next
                i += 1
            if end == None:
                break
            start = pre.next # 当前k个节点的第一个节点
            tmp = end.next # 记录下一次k个节点的第一个节点
            end.next = None # 断开第k个之后的节点
            pre.next = reverse(start) # 反转当前k个节点，并与上一段的最后一个节点相连
            start.next = tmp # 更新start，连到下一次k个节点的第一个节点
            pre, end = start, start # 更新pre和end，准备下一次循环
        
        return dummy.next
        
# @lc code=end

