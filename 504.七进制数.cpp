/*
 * @lc app=leetcode.cn id=504 lang=cpp
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
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }

        string flag = "";
        if (num < 0) {
            flag = "-";
            num *= -1;
        }

        string tmp = "";
        while (num > 0) {
            tmp += to_string(num % 7);
            num = num / 7;
        }
        reverse(tmp.begin(), tmp.end());

        return flag + tmp;
    }
};
// @lc code=end

