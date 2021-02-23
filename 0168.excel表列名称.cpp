/*
 * @lc app=leetcode.cn id=168 lang=cpp
 *
 * [168] Excel表列名称
 *
 * https://leetcode-cn.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (35.44%)
 * Likes:    142
 * Dislikes: 0
 * Total Accepted:    14.9K
 * Total Submissions: 42.2K
 * Testcase Example:  '1'
 *
 * 给定一个正整数，返回它在 Excel 表中相对应的列名称。
 * 
 * 例如，
 * 
 * ⁠   1 -> A
 * ⁠   2 -> B
 * ⁠   3 -> C
 * ⁠   ...
 * ⁠   26 -> Z
 * ⁠   27 -> AA
 * ⁠   28 -> AB 
 * ⁠   ...
 * 
 * 
 * 示例 1:
 * 
 * 输入: 1
 * 输出: "A"
 * 
 * 
 * 示例 2:
 * 
 * 输入: 28
 * 输出: "AB"
 * 
 * 
 * 示例 3:
 * 
 * 输入: 701
 * 输出: "ZY"
 * 
 * 
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        while (n > 0) {
            // n - 1 使得是 0 - 25 对应 A - Z， 转为26进制
            int remainder = (n - 1) % 26;
            res = (char)((int)'A' + remainder) + res;
            n = (n - 1) / 26;
        }
        return res;
    }
};
// @lc code=end

