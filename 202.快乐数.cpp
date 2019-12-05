/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 *
 * https://leetcode-cn.com/problems/happy-number/description/
 *
 * algorithms
 * Easy (55.86%)
 * Likes:    180
 * Dislikes: 0
 * Total Accepted:    34.3K
 * Total Submissions: 61.4K
 * Testcase Example:  '19'
 *
 * 编写一个算法来判断一个数是不是“快乐数”。
 * 
 * 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
 * 1。如果可以变为 1，那么这个数就是快乐数。
 * 
 * 示例: 
 * 
 * 输入: 19
 * 输出: true
 * 解释: 
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    bool isHappy(int n) {
        // 总会在循环内，即快慢指针总会相等，看相等时是否为1
        int fast = n, slow = n;
        int fast_tmp = 0, slow_tmp = 0;
        while (true) {
            while (fast > 0) {
                fast_tmp += (fast % 10) * (fast % 10);
                fast = fast / 10;
            }
            fast = fast_tmp;
            fast_tmp = 0;
            while (fast > 0) {
                fast_tmp += (fast % 10) * (fast % 10);
                fast = fast / 10;
            }
            fast = fast_tmp;
            fast_tmp = 0;

            while (slow > 0) {
                slow_tmp += (slow % 10) * (slow % 10);
                slow = slow / 10;
            }
            slow = slow_tmp;
            slow_tmp = 0;

            if (slow == fast) break;
        }
        return fast == 1 ? true : false;
    }
};
// @lc code=end

