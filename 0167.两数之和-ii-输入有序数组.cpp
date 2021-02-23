/*
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] 两数之和 II - 输入有序数组
 *
 * https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
 *
 * algorithms
 * Easy (50.99%)
 * Likes:    192
 * Dislikes: 0
 * Total Accepted:    49.7K
 * Total Submissions: 97.4K
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
 * 
 * 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
 * 
 * 说明:
 * 
 * 
 * 返回的下标值（index1 和 index2）不是从零开始的。
 * 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
 * 
 * 
 * 示例:
 * 
 * 输入: numbers = [2, 7, 11, 15], target = 9
 * 输出: [1,2]
 * 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
		bool isFind = false;
		while (!numbers.empty()) {
			int cur = numbers[numbers.size() - 1];
			numbers.pop_back();

            if (target > 0 && cur > target) continue; // 优化防止超时

			vector<int>::iterator it = numbers.begin();
			for (; it != numbers.end();) {
				if (*it == target - cur) {
					res.push_back(distance(begin(numbers), it) + 1); // 找到vector中指定值的索引
                    res.push_back(numbers.size() + 1); // cur的位置即当前nums的长度
					isFind = true;
					break;
				}
				it++;
			}
			if (isFind) break;
		}
		return res;
    }
};
// @lc code=end

