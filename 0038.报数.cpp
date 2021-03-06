/*
 * @lc app=leetcode.cn id=38 lang=cpp
 *
 * [38] 报数
 *
 * https://leetcode-cn.com/problems/count-and-say/description/
 *
 * algorithms
 * Easy (53.10%)
 * Likes:    335
 * Dislikes: 0
 * Total Accepted:    57K
 * Total Submissions: 107.2K
 * Testcase Example:  '1'
 *
 * 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
 * 
 * 1.     1
 * 2.     11
 * 3.     21
 * 4.     1211
 * 5.     111221
 * 
 * 
 * 1 被读作  "one 1"  ("一个一") , 即 11。
 * 11 被读作 "two 1s" ("两个一"）, 即 21。
 * 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
 * 
 * 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
 * 
 * 注意：整数顺序将表示为一个字符串。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: 1
 * 输出: "1"
 * 
 * 
 * 示例 2:
 * 
 * 输入: 4
 * 输出: "1211"
 * 
 * 
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
	string countAndSay(int n) {
		string res = "1";
		for (int i = 1; i < n; i++) {
			int cnt = 1;
			string tmp = "";
			char tmpchar = res[0];
			for (int j = 1; j < res.size(); j++) {
				if (tmpchar == res[j]) {
					cnt += 1;
				}
				else {
					tmp += to_string(cnt) + tmpchar;
					cnt = 1;
					tmpchar = res[j];
				}
			}
			tmp += to_string(cnt) + tmpchar;
			res = tmp;
		}
		return res;
	}
};
// @lc code=end

