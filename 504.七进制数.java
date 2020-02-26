/*
 * @lc app=leetcode.cn id=504 lang=java
 *
 * [504] 七进制数
 *
 * https://leetcode-cn.com/problems/base-7/description/
 *
 * algorithms
 * Easy (47.47%)
 * Likes:    33
 * Dislikes: 0
 * Total Accepted:    9.2K
 * Total Submissions: 19K
 * Testcase Example:  '100'
 *
 * 给定一个整数，将其转化为7进制，并以字符串形式输出。
 * 
 * 示例 1:
 * 
 * 
 * 输入: 100
 * 输出: "202"
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: -7
 * 输出: "-10"
 * 
 * 
 * 注意: 输入范围是 [-1e7, 1e7] 。
 * 
 */

// @lc code=start
class Solution {
    public String convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        String flag = "";
        if (num < 0) {
            flag = "-";
            num *= -1;
        }

        String tmp = "";
        while (num > 0) {
            tmp += (num % 7) + "";
            num = num / 7;
        }

        StringBuffer s = new StringBuffer(tmp);
        String res = flag + s.reverse().toString();

        return res;
    }
}
// @lc code=end

