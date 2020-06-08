#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (56.51%)
# Likes:    250
# Dislikes: 0
# Total Accepted:    45.7K
# Total Submissions: 80.3K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 示例 1:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 
# 
# 注意：
# 
# 
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
# 
# 
#

# @lc code=start
class Solution:
    class UnionFind:
        def __init__(self, n):
            self.p = [i for i in range(n)]
        
        def find(self, index):
            while index != self.p[index]:
                self.p[index] = self.p[self.p[index]]
                index = self.p[index]
            return self.p[index] 

        def union(self, index1, index2):
            index1, index2 = self.find(index1), self.find(index2)
            self.p[index1] = index2
        
        def isConn(self, index1, index2):
            return self.find(index1) == self.find(index2)


    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = Solution.UnionFind(len(M))
        for i in range(len(M)):
            for j in range(len(M[0])):
                if j != i and M[i][j] == 1:
                    uf.union(i, j)
        # 需要两次路径压缩才能通过所有用例
        for i in range(len(M)):
            uf.find(i)
        for i in range(len(M)):
            uf.find(i)
        return len(set(uf.p))

# @lc code=end

