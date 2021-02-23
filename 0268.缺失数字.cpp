/*
 * @lc app=leetcode.cn id=268 lang=cpp
 *
 * [268] 缺失数字
 *
 * https://leetcode-cn.com/problems/missing-number/description/
 *
 * algorithms
 * Easy (53.08%)
 * Likes:    183
 * Dislikes: 0
 * Total Accepted:    38.2K
 * Total Submissions: 71.8K
 * Testcase Example:  '[3,0,1]'
 *
 * 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
 * 
 * 示例 1:
 * 
 * 输入: [3,0,1]
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: [9,6,4,2,3,5,7,0,1]
 * 输出: 8
 * 
 * 
 * 说明:
 * 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
 * 
 */

// @lc code=start
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size() + 1;
        float Sn = n * 0 + n * (n - 1) * 1 / 2.0; // 0为首项及等差为1的等差数列求和
        int tmp = accumulate(nums.begin(), nums.end(), 0); // vector所有元素求和
        return (int)Sn - tmp;
    }
};
// @lc code=end

