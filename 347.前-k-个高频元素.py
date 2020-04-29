#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (61.02%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    51K
# Total Submissions: 83.5K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 
# 
# 示例 2:
# 
# 输入: nums = [1], k = 1
# 输出: [1]
# 
# 
# 
# 提示：
# 
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
# 
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素出现频次 O(n)
        cnt = dict()
        for num in nums:
            try:
                cnt[num] += 1
            except:
                cnt[num] = 1
        
        # 将新加入的元素上浮以维护小顶堆 O(logk)
        def shift_up(arr, k):
            """
            arr: 加入新元素后的表示小顶堆的列表，尾部元素为新元素
            k: 加入新元素后小顶堆的规模
            """
            newIndex = k - 1 # 新加入元素在列表的索引位置
            newNode = arr[newIndex] # 新加入元素的节点
            father = (newIndex - 1) // 2 # 新加入元素的父节点在列表中的索引位置
            while newIndex > 0 and arr[father][1] > newNode[1]:
                arr[newIndex] = arr[father]
                newIndex = father
                father = (father - 1) // 2
            arr[newIndex] = newNode

        # 用下沉维护一个规模为k的最小堆 O(logk)
        def shift_down(arr, root, k):
            """
            arr: 表示小顶堆的列表
            root: 堆顶在列表内的索引位置
            k: 堆的规模
            """
            rootNode = arr[root]
            while 2 * root + 1 < k:
                left = 2 * root + 1
                right = 2 * root + 2
                child = left
                if right < k and arr[right][1] < arr[left][1]:
                    child = right
                if rootNode[1] > arr[child][1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
                arr[root] = rootNode

        cnt = list(cnt.items())
        minHeap = list()
        # 从0开始上浮构造规模为k的小顶堆 O(k*logk)
        for i in range(1, k + 1):
            minHeap.append(cnt[i - 1])
            shift_up(minHeap, i)
        # 遍历剩下的元素，若元素比小顶堆的堆顶元素大时，用此元素替换堆顶，并用下沉维护小顶堆 O((n-k)*logk)
        for item in cnt[k:]:
            priority = item[1]
            if priority > minHeap[0][1]:
                minHeap[0] = item
                shift_down(minHeap, 0, k)

        # 总时间复杂度 n + k * logk + (n-k) * logk = n + n*logk, 即 O(nlogk)
        return [node[0] for node in minHeap]
        # 注意：逆序后才是按出现频次从大到小排序的前k个元素，但本题其实不需要逆序

# @lc code=end

