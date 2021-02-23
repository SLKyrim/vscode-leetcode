/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 *
 * https://leetcode-cn.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (51.26%)
 * Likes:    258
 * Dislikes: 0
 * Total Accepted:    47.8K
 * Total Submissions: 93.3K
 * Testcase Example:  '"11"\n"1"'
 *
 * 给定两个二进制字符串，返回他们的和（用二进制表示）。
 * 
 * 输入为非空字符串且只包含数字 1 和 0。
 * 
 * 示例 1:
 * 
 * 输入: a = "11", b = "1"
 * 输出: "100"
 * 
 * 示例 2:
 * 
 * 输入: a = "1010", b = "1011"
 * 输出: "10101"
 * 
 */

// @lc code=start
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
using namespace std;

class Solution {
public:
	string addBinary(string a, string b) {
		vector<int> tmp;
		int tmpnum;
		int carry = 0;

		for (int i = a.size() - 1, j = b.size() - 1; i > -1 && j > -1; i--, j--) {
			tmpnum = (int)(a[i] - '0') + (int)(b[j] - '0') + carry;
			if (tmpnum == 3) {
				tmp.insert(tmp.begin(), 1);
				carry = 1;
			}
			else if (tmpnum == 2) {
				tmp.insert(tmp.begin(), 0);
				carry = 1;
			}
			else {
				tmp.insert(tmp.begin(), tmpnum);
				carry = 0;
			}
		}

		if (a.size() >= b.size()) {
			int more = a.size() - b.size();
			for (int i = more - 1; i > -1; i--) {
				tmpnum = (int)(a[i] - '0') + carry;
				if (tmpnum == 2) {
					tmp.insert(tmp.begin(), 0);
					carry = 1;
				}
				else {
					tmp.insert(tmp.begin(), tmpnum);
					carry = 0;
				}
			}
			if (carry == 1) tmp.insert(tmp.begin(), 1);
		}
		else {
			int more = b.size() - a.size();
			for (int i = more - 1; i > -1; i--) {
				tmpnum = (int)(b[i] - '0') + carry;
				if (tmpnum == 2) {
					tmp.insert(tmp.begin(), 0);
					carry = 1;
				}
				else {
					tmp.insert(tmp.begin(), tmpnum);
					carry = 0;
				}
			}
			if (carry == 1) tmp.insert(tmp.begin(), 1);
		}

		stringstream ss;
		string res;
		copy(tmp.begin(), tmp.end(), ostream_iterator<int>(ss, ""));
		res = ss.str();

		return res;
	}
};
// @lc code=end

