#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新21点
#
# https://leetcode-cn.com/problems/new-21-game/description/
#
# algorithms
# Medium (27.03%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 8.5K
# Testcase Example:  '10\n1\n10'
#
# 爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
# 
# 爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。
# 每次抽取都是独立的，其结果具有相同的概率。
# 
# 当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
# 
# 示例 1：
# 
# 输入：N = 10, K = 1, W = 10
# 输出：1.00000
# 说明：爱丽丝得到一张卡，然后停止。
# 
# 示例 2：
# 
# 输入：N = 6, K = 1, W = 10
# 输出：0.60000
# 说明：爱丽丝得到一张卡，然后停止。
# 在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
# 
# 示例 3：
# 
# 输入：N = 21, K = 17, W = 10
# 输出：0.73278
# 
# 提示：
# 
# 
# 0 <= K <= N <= 10000
# 1 <= W <= 10000
# 如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。
# 此问题的判断限制时间已经减少。
# 
# 
#

# @lc code=start
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0 for _ in range(K + W)] # dp[i]表示得分为i时最后得分不超过N的概率，本题求dp[0]
        # 先对得分[K, K+W-1]的范围初始化，最高得分K+W-1，从K-1抽到W获得
        for i in range(K, K+W):
            dp[i] = 0 if i > N else 1
        
        # 特殊情况，对得分K-1初始化，dp[K-1] = [min(N, K-1+W) - (K-1)] / W
        # 其中[min(N, K-1+W) - (K-1)]表示不超过N的情况数
        dp[K-1] = (min(N, K-1+W) - (K-1)) / W

        # 一般情况，状态转移方程dp[x] = sum(dp[x+1:x+W+1]) / W
        # 当时求sum时，若W很大，则时间复杂度高，因此做差项
        # dp[x+1] = sum(dp[(x+1)+1:(x+1)+W+1]) / W
        # dp[x] - dp[x+1] = (dp[x+1] - dp[x+W+1]) / W
        # dp[x] = dp[x+1] + (dp[x+1] - dp[x+W+1]) / W 对 x < K-1 成立
        # 因为当x = K-1时，dp[K-1] = dp[K] + (dp[K] - dp[K+W]) / W， 但是dp没有索引[K+W]，故需要上面的特殊情况初始化
        for i in range(K-2, -1, -1):
            dp[i] = dp[i+1] + (dp[i+1] - dp[i+W+1]) / W
        
        return dp[0]


# @lc code=end

