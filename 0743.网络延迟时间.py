#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
# https://leetcode-cn.com/problems/network-delay-time/description/
#
# algorithms
# Medium (45.00%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 30.8K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 有 N 个网络节点，标记为 1 到 N。
# 
# 给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w
# 是一个信号从源节点传递到目标节点的时间。
# 
# 现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# 输出：2
# 
# 
# 
# 
# 注意:
# 
# 
# N 的范围在 [1, 100] 之间。
# K 的范围在 [1, N] 之间。
# times 的长度在 [1, 6000] 之间。
# 所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。
# 
# 
#

# @lc code=start
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        vis = [False] * (N + 1) # 记录访问过的节点（即已求出与K节点最短距离的节点）
        dist = {node : float("inf") for node in range(1, N+1)}
        dist[K] = 0
        while True:
            cur_node = -1
            cur_dist = float("inf")
            # 选择一个当前距离K节点最短的节点node来做BFS
            for node in range(1, N+1):
                if not vis[node] and dist[node] < cur_dist:
                    cur_node = node
                    cur_dist = dist[node]
            if cur_node == -1:
                break
            vis[cur_node] = True
            # 更新与节点node邻接的节点到K节点的距离
            for v, w in adj[cur_node]:
                dist[v] = min(dist[v], dist[cur_node] + w)
        res = max(dist.values())
        return res if res < float("inf") else -1

# @lc code=end

