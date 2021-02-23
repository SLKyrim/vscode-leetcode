/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
 *
 * https://leetcode-cn.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (40.90%)
 * Likes:    108
 * Dislikes: 0
 * Total Accepted:    13.5K
 * Total Submissions: 32.9K
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
 * 
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
 * 
 * 示例1:
 * 
 * 输入: pattern = "abba", str = "dog cat cat dog"
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入:pattern = "abba", str = "dog cat cat fish"
 * 输出: false
 * 
 * 示例 3:
 * 
 * 输入: pattern = "aaaa", str = "dog cat cat dog"
 * 输出: false
 * 
 * 示例 4:
 * 
 * 输入: pattern = "abba", str = "dog dog dog dog"
 * 输出: false
 * 
 * 说明:
 * 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
 * 
 */

// @lc code=start
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        istringstream iss(str);
        string tmp;
        vector<string> strs;
        map<string, int> hashmap;
        int cnt = 1;
        while (iss >> tmp) {
            strs.push_back(tmp);
            if (hashmap.count(tmp) == 0){
                hashmap[tmp] = cnt;
                cnt += 1;
            }
        }

        if (strs.size() != pattern.size()) return false;

        map<char, int> hashmap2;
        cnt = 1;
        for (int i = 0; i < pattern.size(); i++) {
            if (hashmap2.count(pattern[i]) == 0){
                hashmap2[pattern[i]] = cnt;
                cnt += 1;
            }
        }

        vector<int> v1, v2;
        for (int i = 0; i < strs.size(); i++) {
            if (hashmap[strs[i]] != hashmap2[pattern[i]]) return false;
        } 
        return true;
    }
};
// @lc code=end

