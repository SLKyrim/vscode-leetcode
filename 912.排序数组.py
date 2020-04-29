#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (51.82%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    20.3K
# Total Submissions: 38.1K
# Testcase Example:  '[5,2,3,1]'
#
# 给定一个整数数组 nums，将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 排序算法图解：
        # https://www.sohu.com/a/258291348_291099
        
        # 堆排序 (27.2%)
        # 堆排序是一种选择排序，就是不断地建最大堆（根节点值不小于其孩子节点值），然后将堆顶（即最大值）换到序列末尾，然后继续建堆，换到末尾（换出去的就不算进下一次堆里了），循环
        def sift_down(arr, root, k):
            """
            将arr[:k]做成大顶堆
            arr: 表示堆的列表
            root: 堆顶根节点在列表arr内的索引位置
            k: 堆的大小
            """
            root_val = arr[root]
            while 2 * root + 1 < k:
                left = 2 * root + 1 # root左孩子在arr中的索引位置
                right = 2 * root + 2 # root右孩子在arr中的索引位置
                child = left
                if right < k and arr[left] < arr[right]:
                    child = right # 若右孩子在堆内且比左孩子大
                if root_val < arr[child]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = root_val

        k = len(nums)
        # 从倒数第二层最右边的节点开始下沉做大顶堆
        # 由堆是完全二叉树的性质得：倒数第二层最右边的节点在列表内索引为(k-1)//2
        for i in range((k - 1) // 2, -1, -1):
            sift_down(nums, i, k)
        # 堆排序，每次下沉堆规模减1，依次把堆顶最大值放到尾部
        for i in range(k - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sift_down(nums, 0, i)
        return nums


        
        # # 计数排序 (87.18%)
        # # 当序列由整数组成，且相对密集时非常快
        # # 做一个计数器c记录序列中数出现的个数
        # numMax = max(nums)
        # numMin = min(nums)
        # c = [0 for i in range(numMax - numMin + 1)]
        # for num in nums:
        #     c[num - numMin] += 1
        # ind = 0
        # for i in range(numMax - numMin + 1):
        #     for j in range(c[i]):
        #         nums[ind] = i + numMin
        #         ind += 1
        # return nums

        # # 归并排序 (32.13%)
        # # 将两个排好序的子序列合成一个排好序的总数组
        # def mergeSort(left, right):
        #     """
        #     left, right: 排好序的子序列
        #     """
        #     res = []
        #     l, r = 0, 0
        #     while l < len(left) and r < len(right):
        #         if left[l] < right[r]:
        #             res.append(left[l])
        #             l += 1
        #         else:
        #             res.append(right[r])
        #             r += 1
        #     while l < len(left):
        #         res.append(left[l])
        #         l += 1
        #     while r < len(right):
        #         res.append(right[r])
        #         r += 1
        #     return res

        # def merge(arr):
        #     if len(arr) <= 1:
        #         return arr
        #     mid = len(arr) // 2
        #     left = merge(arr[:mid])
        #     right = merge(arr[mid:])
        #     return mergeSort(left, right)

        # return merge(nums)


        # # 快速排序 (62.04%)
        # # 选择一个基准（pivot），通常为序列首元素
        # # 将小于此基准的元素做成左子序列，大于基准的做成右子序列
        # # 递归地快速排序左右子序列
        # n = len(nums)
        # if n <= 1:
        #     return nums
        # pivot = nums[0]
        # left = [x for x in nums[1:] if x <= pivot]
        # right = [x for x in nums[1:] if x > pivot]
        # return self.sortArray(left) + [pivot] + self.sortArray(right)


        # # 选择排序 (超时)
        # # 选择一个最小的放在最前面
        # n = len(nums)
        # for i in range(n):
        #     curMin = nums[i]
        #     curInd = i
        #     for j in range(i, n):
        #         if nums[j] < curMin:
        #             curMin = nums[j]
        #             curInd = j
        #     nums[i], nums[curInd] = nums[curInd], nums[i]
        # return nums


        # # 冒泡排序（超时）
        # n = len(nums)
        # for i in range(n):
        #     isOK = True
        #     for j in range(1, n - i):
        #         if nums[j - 1] > nums[j]:
        #             nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #             isOK = False
        #     if isOK:
        #         break
        # return nums

        # # 调用排序函数 (97.47%)
        # return sorted(nums)
        
# @lc code=end

