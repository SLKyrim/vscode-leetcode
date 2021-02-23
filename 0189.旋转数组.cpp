/*
 * @lc app=leetcode.cn id=189 lang=cpp
 *
 * [189] 旋转数组
 *
 * https://leetcode-cn.com/problems/rotate-array/description/
 *
 * algorithms
 * Easy (39.30%)
 * Likes:    414
 * Dislikes: 0
 * Total Accepted:    78.2K
 * Total Submissions: 198.9K
 * Testcase Example:  '[1,2,3,4,5,6,7]\n3'
 *
 * 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
 * 
 * 示例 1:
 * 
 * 输入: [1,2,3,4,5,6,7] 和 k = 3
 * 输出: [5,6,7,1,2,3,4]
 * 解释:
 * 向右旋转 1 步: [7,1,2,3,4,5,6]
 * 向右旋转 2 步: [6,7,1,2,3,4,5]
 * 向右旋转 3 步: [5,6,7,1,2,3,4]
 * 
 * 
 * 示例 2:
 * 
 * 输入: [-1,-100,3,99] 和 k = 2
 * 输出: [3,99,-1,-100]
 * 解释: 
 * 向右旋转 1 步: [99,-1,-100,3]
 * 向右旋转 2 步: [3,99,-1,-100]
 * 
 * 说明:
 * 
 * 
 * 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
 * 要求使用空间复杂度为 O(1) 的 原地 算法。
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int tmp;
        for (int i = 0; i < k; i++) {
            tmp = nums[nums.size() - 1];
            nums.pop_back();
            nums.insert(nums.begin(), tmp);
        }
        // vector<int>::iterator it = nums.end();
        // for (int i = 0; i < k; i++) it--;
        // nums.insert(nums.begin(), it, nums.end()); 
        // it = nums.end(); // insert后it不再指向原位置，需要重新定位
        // for (int i = 0; i < k; i++) it--;
        // for (; it != nums.end();) it = nums.erase(it);
        // return;
    }
};
// @lc code=end

