/*
 * @lc app=leetcode.cn id=414 lang=java
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
// import java.util.Set;
// import java.util.HashSet;
// import java.util.Collections;
// import java.util.ArrayList;
// import java.util.List;

// class Solution {
//     public int thirdMax(int[] nums) {
//         Set<Integer> tmp = new HashSet<>();
//         for (int num : nums) {
//             tmp.add(num);
//         }
//         if (tmp.size() < 3) {
//             return Collections.max(tmp);
//         }
//         List<Integer> tmp2 = new ArrayList<>();
//         for (int num : tmp) {
//             tmp2.add(num);
//         }
//         Collections.sort(tmp2);
//         Collections.reverse(tmp2);
//         return tmp2.get(2);
//     }
// }


import java.util.PriorityQueue;

class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.add(num);
        }
        if (pq.size() < 3) {
            return pq.peek();
        }
        int res = pq.peek();
        for (int i = 0; i < pq.size() - 3; i++) {
            res = pq.remove();
        }
        return res;
    }
}
// @lc code=end

