/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 *
 * https://leetcode-cn.com/problems/move-zeroes/description/
 *
 * algorithms
 * Easy (57.66%)
 * Likes:    439
 * Dislikes: 0
 * Total Accepted:    83.4K
 * Total Submissions: 144.3K
 * Testcase Example:  '[0,1,0,3,12]'
 *
 * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
 * 
 * 示例:
 * 
 * 输入: [0,1,0,3,12]
 * 输出: [1,3,12,0,0]
 * 
 * 说明:
 * 
 * 
 * 必须在原数组上操作，不能拷贝额外的数组。
 * 尽量减少操作次数。
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        for (vector<int>::iterator it = nums.begin(); it != nums.end(); ) {
            if (*it == 0) it = nums.erase(it);
            else it++;
        }
        int m = nums.size(); 
        while (n - m > 0) { // 不能直接由n - nums.size()得，因为nums.size()在循环过程中会改变
            nums.push_back(0);
            n--;
        }
    }
};
// @lc code=end

