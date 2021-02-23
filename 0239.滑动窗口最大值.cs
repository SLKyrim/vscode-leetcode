/*
 * @lc app=leetcode.cn id=239 lang=csharp
 *
 * [239] 滑动窗口最大值
 *
 * https://leetcode-cn.com/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (49.00%)
 * Likes:    797
 * Dislikes: 0
 * Total Accepted:    118.5K
 * Total Submissions: 239.2K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
 * 个数字。滑动窗口每次只向右移动一位。
 * 
 * 返回滑动窗口中的最大值。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
 * 输出：[3,3,5,5,6,7]
 * 解释：
 * 滑动窗口的位置                最大值
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1], k = 1
 * 输出：[1]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [1,-1], k = 1
 * 输出：[1,-1]
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：nums = [9,11], k = 2
 * 输出：[11]
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：nums = [4,-2], k = 2
 * 输出：[4]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * -10^4 
 * 1 
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k)
    {
        int n = nums.Length;

        // C#中List可以实现双向队列Deque的功能
        List<int> deque = new List<int>();

        for (int i = 0; i < k; i++)
        {
            // while循环保证deque最左边的是最大值的索引
            while (deque.Count != 0 && nums[i] >= nums[deque[deque.Count - 1]])
                deque.RemoveAt(deque.Count - 1);
            deque.Add(i);
        }

        // 将第一个滑窗的最大值加入res
        List<int> res = new List<int>{ nums[deque[0]] };

        for (int i = k; i < n; i++)
        {
            while (deque.Count != 0 && nums[i] >= nums[deque[deque.Count - 1]])
                deque.RemoveAt(deque.Count - 1);
            deque.Add(i);
            // 当队列中的最大值索引不在滑窗范围内时需要删除
            // 保证deque最左边是滑窗范围内的最大值索引
            while (deque[0] <= i - k)
                deque.RemoveAt(0);
            res.Add(nums[deque[0]]);
        }
        return res.ToArray();
    }
}
// @lc code=end

