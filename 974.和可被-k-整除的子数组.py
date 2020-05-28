#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (38.10%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 43.3K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
# 
# 
# 
# 示例：
# 
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#

# @lc code=start
import collections

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        tmp = collections.defaultdict(int)
        tmp[0] = 1 # 包括了前缀和本身也能被K整除的情况
        
        preSum = 0 # 记录前缀和
        res = 0
        for i in range(len(A)):
            preSum += A[i]
            # cur = preSum if preSum >= 0 else -preSum
            mod = preSum % K
            if tmp[mod] > 0:
                # 同余定理：当a-b能被k整除时，a%k == b%k
                # 当前前缀和a模K等于之前的前缀和b模K时，说明a-b能被K整除，
                # 那么有多少个前缀和b就说明有多少个和为a-b的子数组能被K整除
                res += tmp[mod]
            tmp[mod] += 1
        return res
    
# @lc code=end

