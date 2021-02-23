/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
 *
 * https://leetcode-cn.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (39.10%)
 * Likes:    306
 * Dislikes: 0
 * Total Accepted:    46.9K
 * Total Submissions: 119.9K
 * Testcase Example:  '[1,2]'
 *
 * 请判断一个链表是否为回文链表。
 * 
 * 示例 1:
 * 
 * 输入: 1->2
 * 输出: false
 * 
 * 示例 2:
 * 
 * 输入: 1->2->2->1
 * 输出: true
 * 
 * 
 * 进阶：
 * 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head) return true;
        ListNode* tmp = head;
        vector<int> tmpv;
        while (tmp) {
            tmpv.push_back(tmp->val);
            tmp = tmp->next;
        }
        for (int i = 0; i < tmpv.size()/2; i++) {
            if (tmpv[i] != tmpv[tmpv.size() - 1 - i]) return false;
        }
        return true;
    }
};
// @lc code=end

