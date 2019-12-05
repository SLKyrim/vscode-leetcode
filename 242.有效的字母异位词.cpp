/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 *
 * https://leetcode-cn.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (56.81%)
 * Likes:    125
 * Dislikes: 0
 * Total Accepted:    56.5K
 * Total Submissions: 99.3K
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
 * 
 * 示例 1:
 * 
 * 输入: s = "anagram", t = "nagaram"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: s = "rat", t = "car"
 * 输出: false
 * 
 * 说明:
 * 你可以假设字符串只包含小写字母。
 * 
 * 进阶:
 * 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
 * 
 */

// @lc code=start
#include <string>
#include <map>
#include <set>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        map<char, int> map_s, map_t;
        set<char> tmp;
        for (int i = 0; i < s.size(); i++) {
            if (map_s.count(s[i]) == 0) map_s.insert(pair<char, int>(s[i], 1));
            else map_s[s[i]] += 1;
            if (map_t.count(t[i]) == 0) map_t.insert(pair<char, int>(t[i], 1));
            else map_t[t[i]] += 1;
            tmp.insert(s[i]);
            tmp.insert(t[i]);
        }
        for (set<char>::iterator it = tmp.begin(); it != tmp.end(); it++) {
            if (map_s[*it] != map_t[*it]) return false;
        }
        return true;
    }
};
// @lc code=end

