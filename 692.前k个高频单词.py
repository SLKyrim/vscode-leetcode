#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
# https://leetcode-cn.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (51.13%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 22.1K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
# 
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
# 
# 示例 1：
# 
# 
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
# ⁠   注意，按字母顺序 "i" 在 "love" 之前。
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
# k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
# ⁠   出现次数依次为 4, 3, 2 和 1 次。
# 
# 
# 
# 
# 注意：
# 
# 
# 假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
# 输入的单词均由小写字母组成。
# 
# 
# 
# 
# 扩展练习：
# 
# 
# 尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
# 
# 
#

# @lc code=start
import collections
import heapq

class Solution:
    def topKFrequent(self, words, k: int):
        # 调用库函数 56.98%
        cnt = collections.Counter(words)
        heap = [(-freq, word) for word, freq in cnt.items()] # 负号是因为要按freq降序输出,而默认是升序
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]


        # 手写堆排序 29.68%
        # # 统计元素出现频次 O(n)
        # cnt = dict()
        # for word in words:
        #     try:
        #         cnt[word] += 1
        #     except:
        #         cnt[word] = 1

        # # 将新加入的元素上浮以维护小顶堆 O(logk)
        # def shift_up(arr, k):
        #     """
        #     arr: 加入新元素后的表示小顶堆的列表，尾部元素为新元素
        #     k: 加入新元素后小顶堆的规模
        #     """
        #     newIndex = k - 1  # 新加入元素在列表的索引位置
        #     newNode = arr[newIndex]  # 新加入元素的节点
        #     father = (newIndex - 1) // 2  # 新加入元素的父节点在列表中的索引位置
        #     while newIndex > 0:
        #         if arr[father][1] > newNode[1]:
        #             arr[newIndex] = arr[father]
        #             newIndex = father
        #             father = (father - 1) // 2
        #         # 当新加入词次数与堆内节点相同时，保证字典序大的节点当父节点
        #         # 从而保证替换堆顶
        #         elif arr[father][1] == newNode[1]:
        #             if arr[father][0] < newNode[0]:
        #                 arr[newIndex] = arr[father]
        #                 newIndex = father
        #                 father = (father - 1) // 2
        #             else:
        #                 break
        #         else:
        #             break
        #     arr[newIndex] = newNode

        # # 用下沉维护一个规模为k的最小堆 O(logk)
        # def shift_down(arr, root, k):
        #     """
        #     arr: 表示小顶堆的列表
        #     root: 堆顶在列表内的索引位置
        #     k: 堆的规模
        #     """
        #     rootNode = arr[root]
        #     while 2 * root + 1 < k:
        #         left = 2 * root + 1
        #         right = 2 * root + 2
        #         child = left
        #         if right < k and arr[right][1] < arr[left][1]:
        #             child = right
        #         # 当左右孩子词频相同时，保证字典序大的与下沉节点调换
        #         if right < k and arr[right][1] == arr[left][1]:
        #             if arr[right][0] > arr[left][0]:
        #                 child = right
        #         if rootNode[1] > arr[child][1]:
        #             arr[root] = arr[child]
        #             root = child
        #         elif rootNode[1] == arr[child][1]:
        #             # 节点与根节点词频相同时，字典序小的节点与根节点调换，保证字典序大的在堆顶
        #             if rootNode[0] < arr[child][0]:
        #                 arr[root] = arr[child]
        #                 root = child
        #             else:
        #                 break
        #         else:
        #             break
        #         arr[root] = rootNode

        # cnt = list(cnt.items())
        # minHeap = list()
        # # 从0开始上浮构造规模为k的小顶堆 O(k*logk)
        # for i in range(1, k + 1):
        #     minHeap.append(cnt[i - 1])
        #     shift_up(minHeap, i)
        # # 遍历剩下的元素，若元素比小顶堆的堆顶元素大时，用此元素替换堆顶，并用下沉维护小顶堆 O((n-k)*logk)
        # for item in cnt[k:]:
        #     priority = item[1]
        #     if priority > minHeap[0][1]:
        #         minHeap[0] = item
        #         shift_down(minHeap, 0, k)
        #     # 词频相同时，字典序小的入堆替换堆顶
        #     elif priority == minHeap[0][1]:
        #         if minHeap[0][0] < item[0]:
        #             continue
        #         minHeap[0] = item
        #         shift_down(minHeap, 0, k)

        # # sorted排序为O(k*logk), 故总时间仍为 O(nlogk)
        # return [node[0] for node in sorted(minHeap, key=lambda x: (-x[1],x[0]))]
                  
# @lc code=end

