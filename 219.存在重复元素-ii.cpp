/*
 * @lc app=leetcode.cn id=219 lang=cpp
 *
 * [219] 存在重复元素 II
 *
 * https://leetcode-cn.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (36.36%)
 * Likes:    118
 * Dislikes: 0
 * Total Accepted:    25.6K
 * Total Submissions: 70.3K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
 * 的差的绝对值最大为 k。
 * 
 * 示例 1:
 * 
 * 输入: nums = [1,2,3,1], k = 3
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入: nums = [1,0,1,1], k = 1
 * 输出: true
 * 
 * 示例 3:
 * 
 * 输入: nums = [1,2,3,1,2,3], k = 2
 * 输出: false
 * 
 */

// @lc code=start
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0 || nums.size() < 2) return false;
        if (k >= nums.size()) k = nums.size() - 1;

        unordered_set<int> tmp;
        for (int i = 0; i < nums.size(); i++) {
            if (i > k) tmp.erase(nums[i - k - 1]); // unordered_set按值删除
            if (tmp.find(nums[i]) != tmp.end()) return true;
            tmp.insert(nums[i]);
        }
        return false;
        
        // // 超时
        // if (k >= nums.size()){
        //     for (int i = 0; i < nums.size() - 1; i++) {
        //         for (int j = i+1; j <nums.size(); j++) {
        //             if (nums[i] == nums[j]) return true;
        //         }
        //     }
        //     return false;
        // }
        // for (int i = 0; i < nums.size() - k; i++) {
        //     for (int j = 1; j <= k; j++) {
        //         if (nums[i] == nums[i+j]) return true;
        //     }
        // }
        // for (int i = nums.size() - k; i < nums.size() - 1; i++) {
        //     for (int j = i+1; j <nums.size(); j++) {
        //         if (nums[i] == nums[j]) return true;
        //     }
        // }
        // return false;
    }
};
// @lc code=end

