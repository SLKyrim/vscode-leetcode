#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (62.73%)
# Likes:    534
# Dislikes: 0
# Total Accepted:    136.7K
# Total Submissions: 216K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def shift_up(heap, k):
            newInd = k - 1
            newNode = heap[newInd]
            father = (newInd - 1) // 2
            while newInd > 0 and heap[father] > newNode:
                heap[newInd] = heap[father]
                newInd = father
                father = (father - 1) // 2
            heap[newInd] = newNode

        def shift_down(heap, root, k):
            rootNode = heap[root]
            while 2*root+1 < k:
                left = 2*root + 1
                right = 2*root + 2
                child = left
                if right < k and heap[right] < heap[left]:
                    child = right
                if rootNode > heap[child]:
                    heap[root] = heap[child]
                    root = child
                else:
                    break
                heap[root] = rootNode

        heap = []
        for i in range(k):
            heap.append(nums[i])
            shift_up(heap, i+1)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                shift_down(heap, 0, k)
        return heap[0]

# @lc code=end

