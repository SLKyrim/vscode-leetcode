#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#
# https://leetcode-cn.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (30.24%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 7.5K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# 给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target
# 的元组 i, j, k 的数量。
# 
# 由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举（A[i]，A[j]，A[k]）：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
# 
# 
# 示例 2：
# 
# 输入：A = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# A[i] = 1，A[j] = A[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300
# 
# 
#

# @lc code=start
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        # 数学方法 
        # 思路：先统计A中每种数出现的次数；
        # 对三种数x,y,z,共有4中情况：
        # 1、x!=y!=z, 组合数为 cnt[x] * cnt[y] * cnt[z]
        # 2、x==y!=z, 组合数为 C(2,m) * cnt[z]，其中m为等于x和y的数的个数
        # 3、x!=y==z, 组合数为 cnt[x] * C(2,m)，其中m为等于z和y的数的个数
        # 4、x==y==z, 组合数为 C(3,m) = m!/((m-3)!*3!) = m * (m - 1) * (m - 2) / 3!, 其中m为等于x和y和z的个数
        n = len(A)
        cnt = [0] * 101
        for i in range(n):
            cnt[A[i]] += 1
        
        res = 0   
        for x in range(101):
            # 1、x!=y!=z
            for y in range(x+1, 101):
                z = target - x - y
                if y < z <= 100: # 限制y和z的大小条件，避免重复计算
                    res += cnt[x] * cnt[y] * cnt[z]
            # 2、x==y!=z
            z = target - 2 * x
            if x < z <= 100: # 限制x和z的大小条件，避免重复计算
                C = cnt[x] * (cnt[x] - 1) // 2
                res += C * cnt[z]
            # 3、x!=y==z
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100: # 限制x和y的大小条件，避免重复计算
                    C = cnt[y] * (cnt[y] - 1) // 2
                    res += cnt[x] * C
        # 4、x==y==z
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                res += cnt[x] * (cnt[x] - 1) * (cnt[x] - 2) // 6
        
        return res % (10**9+7)
                

        # # 三指针 超时（69/70）
        # # 时间复杂度 O(N**2): for循环一个O(N)再加上里面的while循环一个O(N)
        # # 思路：三个索引i,j,k，固定i，找满足A[j] + A[k] == target - A[i]的j和k的组合数。
        # # 对每个i，j = i+1, k = n - 1，j从左往右搜索，k从右往左搜索
        # n = len(A)
        # res = 0
        # A = sorted(A) # 先排序
        # for i in range(n - 2):
        #     j = i + 1
        #     k = n - 1
        #     t = target - A[i]
        #     while j < k:
        #         if A[j] + A[k] < t:
        #             j += 1
        #         elif A[j] + A[k] > t:
        #             k -= 1
        #         else:
        #             if A[j] != A[k]:
        #                 cnt_j, cnt_k = 1, 1
        #                 while j < k and A[j + 1] == A[j]:
        #                     cnt_j += 1
        #                     j += 1
        #                 while j < k and A[k - 1] == A[k]:
        #                     cnt_k += 1
        #                     k -= 1
        #                 res += cnt_j * cnt_k
        #                 # 下面这俩容易漏从而造成死循环
        #                 j += 1
        #                 k -= 1
        #             else:
        #                 # m个数中的两两组合数 C(2,m) = m!/((m-2)!2!) = m*(m-1)/2
        #                 m = k - j + 1
        #                 res += m * (m - 1) // 2
        #                 break
        # return res % (10**9+7)
        
# @lc code=end

