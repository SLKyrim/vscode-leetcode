/*
 * @lc app=leetcode.cn id=399 lang=csharp
 *
 * [399] 除法求值
 *
 * https://leetcode-cn.com/problems/evaluate-division/description/
 *
 * algorithms
 * Medium (55.03%)
 * Likes:    445
 * Dislikes: 0
 * Total Accepted:    30.9K
 * Total Submissions: 51.9K
 * Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
 *
 * 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和
 * values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
 * 
 * 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj
 * = ? 的结果作为答案。
 * 
 * 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0
 * 替代这个答案。
 * 
 * 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
 * [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
 * 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
 * 解释：
 * 条件：a / b = 2.0, b / c = 3.0
 * 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
 * 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
 * queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
 * 输出：[3.75000,0.40000,5.00000,0.20000]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：equations = [["a","b"]], values = [0.5], queries =
 * [["a","b"],["b","a"],["a","c"],["x","y"]]
 * 输出：[0.50000,2.00000,-1.00000,-1.00000]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * equations[i].length == 2
 * 1 i.length, Bi.length 
 * values.length == equations.length
 * 0.0 < values[i] 
 * 1 
 * queries[i].length == 2
 * 1 j.length, Dj.length 
 * Ai, Bi, Cj, Dj 由小写英文字母与数字组成
 * 
 * 
 */

// @lc code=start
public class Solution
{
    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries)
    {
        int n = equations.Count;

        UnionFind unionFind = new UnionFind(2 * n);

        Dictionary<string, int> hashMap = new Dictionary<string, int>(2 * n);
        int id = 0;
        for (int i = 0; i < n; i++)
        {
            IList<string> equation = equations[i];
            string var1 = equation[0];
            string var2 = equation[1];

            if (!hashMap.ContainsKey(var1))
            {
                hashMap.Add(var1, id);
                id++;
            }
            if (!hashMap.ContainsKey(var2))
            {
                hashMap.Add(var2, id);
                id++;
            }
            unionFind.union(hashMap[var1], hashMap[var2], values[i]);
        }

        int m = queries.Count;
        double[] res = new double[m];
        for (int i = 0; i < m; i++)
        {
            string var1 = queries[i][0];
            string var2 = queries[i][1];

            if (!hashMap.ContainsKey(var1) || !hashMap.ContainsKey(var2))
            {
                res[i] = -1.0;
            }
            else
            {
                int id1 = hashMap[var1];
                int id2 = hashMap[var2];
                res[i] = unionFind.isConnected(id1, id2);
            }
        }
        return res;
    }

    private class UnionFind
    {
        private int[] parent;

        private double[] weight;

        public UnionFind(int n)
        {
            this.parent = new int[n];
            this.weight = new double[n];
            for (int i = 0; i < n; i++)
            {
                parent[i] = i;
                weight[i] = 1.0;
            }
        }

        public int find(int x)
        {
            if (x != parent[x])
            {
                int origin = parent[x];
                parent[x] = find(parent[x]);
                weight[x] *= weight[origin];
            }
            return parent[x];
        }

        public void union(int x, int y, double value)
        {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY)
                return;

            parent[rootX] = rootY;
            weight[rootX] = weight[y] * value / weight[x];
        }

        public double isConnected(int x, int y)
        {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY)
                return weight[x] / weight[y];
            else
                return -1.0;
        }
    }
}
// @lc code=end

