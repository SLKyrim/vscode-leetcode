/*
 * @lc app=leetcode.cn id=187 lang=cpp
 *
 * [187] 重复的DNA序列
 *
 * https://leetcode-cn.com/problems/repeated-dna-sequences/description/
 *
 * algorithms
 * Medium (42.60%)
 * Likes:    60
 * Dislikes: 0
 * Total Accepted:    9.9K
 * Total Submissions: 22.9K
 * Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
 *
 * 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
 * 中的重复序列有时会对研究非常有帮助。
 * 
 * 编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
 * 输出：["AAAAACCCCC", "CCCCCAAAAA"]
 * 
 */

// @lc code=start
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if (s.size() < 10) {
            return res;
        }
        map<string, int> mapv;
        for (int i = 0; i < s.size() - 9; i++) {
            string curr = s.substr(i, 10);
            if (mapv.count(curr) == 0) {
                mapv.insert(make_pair(curr, 1));
            }
            else {
                mapv[curr] += 1;
            }
            if (mapv[curr] == 2) {
                res.push_back(curr);
            }
        }
        return res;
    }
};
// @lc code=end

