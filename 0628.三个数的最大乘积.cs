/*
 * @lc app=leetcode.cn id=628 lang=csharp
 *
 * [628] 三个数的最大乘积
 *
 * https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
 *
 * algorithms
 * Easy (50.02%)
 * Likes:    218
 * Dislikes: 0
 * Total Accepted:    39.5K
 * Total Submissions: 78K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [1,2,3]
 * 输出: 6
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [1,2,3,4]
 * 输出: 24
 * 
 * 
 * 注意:
 * 
 * 
 * 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
 * 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int MaximumProduct(int[] nums)
    {
        Array.Sort(nums);
        Array.Reverse(nums);
        int n = nums.Length;
        int front = nums[0] * nums[1] * nums[2];
        int back = nums[0] * nums[n - 1] * nums[n - 2];
        return Math.Max(front, back);
    }
}
// @lc code=end

