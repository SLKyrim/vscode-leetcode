/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 *
 * https://leetcode-cn.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (41.46%)
 * Likes:    122
 * Dislikes: 0
 * Total Accepted:    61.7K
 * Total Submissions: 148.8K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * 
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 * 
 * 示例 1:
 * 
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: "race a car"
 * 输出: false
 * 
 * 
 */

// @lc code=start
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        if (s == "") return true;
        string tmp = "";
        for (char ch : s) {
            if (isalnum(ch)) tmp += ch; // 判断是否为字母和数字字符，若是则添加到tmp字串
        }
        transform(tmp.begin(),tmp.end(),tmp.begin(),::tolower); // 将tmp字串中的大写字母转为小写
        string tmp2 = tmp; // 备份tmp字串
        reverse(tmp.begin(), tmp.end()); // 将tmp字串逆序
        return tmp == tmp2; // 判断两个字符串是否相等
    }
};
// @lc code=end

