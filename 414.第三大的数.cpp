/*
 * @lc app=leetcode.cn id=414 lang=cpp
 *
 * [414] 第三大的数
 *
 * https://leetcode-cn.com/problems/third-maximum-number/description/
 *
 * algorithms
 * Easy (33.37%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    16.7K
 * Total Submissions: 49.3K
 * Testcase Example:  '[3,2,1]'
 *
 * 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [3, 2, 1]
 * 
 * 输出: 1
 * 
 * 解释: 第三大的数是 1.
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [1, 2]
 * 
 * 输出: 2
 * 
 * 解释: 第三大的数不存在, 所以返回最大的数 2 .
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: [2, 2, 3, 1]
 * 
 * 输出: 1
 * 
 * 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
 * 存在两个值为2的数，它们都排第二。
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> tmp;
        for (int num : nums) {
            tmp.insert(num);
        }

        set<int>::iterator it = tmp.begin();
        if (tmp.size() < 3) {
            int tmpNum = *it;
            for (; it != tmp.end(); it++) {
                if (*it > tmpNum) {
                    tmpNum = *it;
                }
            }
            return tmpNum;
        }

        vector<int> tmp2;
        for (; it != tmp.end(); it++) {
            tmp2.push_back(*it);
        }
        sort(tmp2.begin(), tmp2.end(), greater<int>());
        return tmp2[2];
    }
};
// @lc code=end

