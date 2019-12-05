/*
 * @lc app=leetcode.cn id=205 lang=cpp
 *
 * [205] 同构字符串
 *
 * https://leetcode-cn.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (46.53%)
 * Likes:    143
 * Dislikes: 0
 * Total Accepted:    20.7K
 * Total Submissions: 44.5K
 * Testcase Example:  '"egg"\n"add"'
 *
 * 给定两个字符串 s 和 t，判断它们是否是同构的。
 * 
 * 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
 * 
 * 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
 * 
 * 示例 1:
 * 
 * 输入: s = "egg", t = "add"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: s = "foo", t = "bar"
 * 输出: false
 * 
 * 示例 3:
 * 
 * 输入: s = "paper", t = "title"
 * 输出: true
 * 
 * 说明:
 * 你可以假设 s 和 t 具有相同的长度。
 * 
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (check1(s) == check1(t)) {
            if (check2(s) == check2(t)) return true;
        }
        return false;
    }

    int check1(string s) {
        string tmp = "";
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (tmp.find(s[i]) == -1) {
                tmp += s[i];
                res += tmp.size();
            }
            else {
                res += tmp.find(s[i]) + 1;
            }
        }
        return res;
    }

    int check2(string s) {
        string tmp = "";
        string res = "";
        for (int i = 0; i < s.size(); i++) {
            if (tmp.find(s[i]) == -1) {
                tmp += s[i];
                res += to_string(tmp.size());
            }
            else {
                res += to_string(tmp.find(s[i]) + 1);
            }
        }
        return atoi(res.c_str());
    }
};
// @lc code=end

