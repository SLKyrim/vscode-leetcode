/*
 * @lc app=leetcode.cn id=263 lang=cpp
 *
 * [263] 丑数
 *
 * https://leetcode-cn.com/problems/ugly-number/description/
 *
 * algorithms
 * Easy (47.90%)
 * Likes:    78
 * Dislikes: 0
 * Total Accepted:    18.7K
 * Total Submissions: 38.9K
 * Testcase Example:  '6'
 *
 * 编写一个程序判断给定的数是否为丑数。
 * 
 * 丑数就是只包含质因数 2, 3, 5 的正整数。
 * 
 * 示例 1:
 * 
 * 输入: 6
 * 输出: true
 * 解释: 6 = 2 × 3
 * 
 * 示例 2:
 * 
 * 输入: 8
 * 输出: true
 * 解释: 8 = 2 × 2 × 2
 * 
 * 
 * 示例 3:
 * 
 * 输入: 14
 * 输出: false 
 * 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
 * 
 * 说明：
 * 
 * 
 * 1 是丑数。
 * 输入不会超过 32 位有符号整数的范围: [−2^31,  2^31 − 1]。
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	bool isUgly(int num) {
		if (num <= 0) return false;
        if (num == 1) return true;
		vector<long> ugly(1, 1);
		int m2 = 0, m3 = 0, m5 = 0;
		while (true) {
			long tmp = min(ugly[m2] * 2, min(ugly[m3] * 3, ugly[m5] * 5));
			ugly.push_back(tmp);
			while (ugly[m2] * 2 <= tmp) m2 += 1;
			while (ugly[m3] * 3 <= tmp) m3 += 1;
			while (ugly[m5] * 5 <= tmp) m5 += 1;
			if (ugly[ugly.size() - 1] == num) return true;
			if (ugly[ugly.size() - 1] > num) break;
		}
		return false;
	}
};
// @lc code=end

