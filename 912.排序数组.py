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
        
        # 堆排序 (6.03%)
        # 堆排序是一种选择排序，就是不断地建最大堆（根节点值不小于其孩子节点值），然后将堆顶（即最大值）换到序列末尾，然后继续建堆，换到末尾（换出去的就不算进下一次堆里了），循环
        def buildHeap(arr, n, i):
            """
            做最大堆
            arr: 表示当前堆的数组
            n: 堆内元素个数
            i: 堆顶位置 
            """
            top = i
            l = 2 * i + 1 # 堆顶左子树根节点位置
            r = 2 * i + 2 # 堆顶右子树根节点位置

            # 遗留问题：这里的n为什么不能用len(arr)代替从而减少传递参数的数量
            # 左子树根大于堆顶，换到堆顶
            if l < n and arr[i] < arr[l]:
                top = l
            
            # 右子树根大于堆顶，换到堆顶
            if r < n and arr[top] < arr[r]:
                top = r
            
            # 若堆顶已替换，则继续递归；否则最大堆已做成，结束递归
            if top != i:
                arr[top], arr[i] = arr[i], arr[top]
                buildHeap(arr, n, top)

        def heapSort(arr):
            """
            对arr进行堆排序
            """
            n = len(arr)

            # 从堆底把子堆做成最大堆，逐步把整个数组做成最大堆
            for i in range(n - 1, -1, -1):
                buildHeap(arr, n, i)

            # 每次做完重新做完最大堆后，arr[0]即堆顶最大值，arr[i]即堆底，arr[i]之后的都是弹出堆排序好的序列
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i] # 堆底和堆顶交换
                buildHeap(arr, i, 0) # 弹出堆底后重新做最大堆
            
            return arr

        return heapSort(nums)

        
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

