/*
 * @lc app=leetcode.cn id=203 lang=cpp
 *
 * [203] 移除链表元素
 *
 * https://leetcode-cn.com/problems/remove-linked-list-elements/description/
 *
 * algorithms
 * Easy (42.81%)
 * Likes:    305
 * Dislikes: 0
 * Total Accepted:    45.9K
 * Total Submissions: 107.2K
 * Testcase Example:  '[1,2,6,3,4,5,6]\n6'
 *
 * 删除链表中等于给定值 val 的所有节点。
 * 
 * 示例:
 * 
 * 输入: 1->2->6->3->4->5->6, val = 6
 * 输出: 1->2->3->4->5
 * 
 * 
 */

// @lc code=start
#include <iostream>
using namespace std;

// // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return head; // 输入head为空时输出
        while (head->val == val) {
            head = head->next;
            if (!head) return head; // 链表全为待删除元素时输出
        }    
        ListNode* tmp = head;
        ListNode* pre;
        
        // 删除链表中指定元素的节点
        while (tmp) {
            if (tmp->val == val) {
                tmp = tmp->next;
                pre->next = tmp;
            }
            else {
                pre = tmp;
                tmp = tmp->next;
            }
        }
        return head;
    }
};
// @lc code=end

