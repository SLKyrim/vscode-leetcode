/*
 * @lc app=leetcode.cn id=695 lang=csharp
 *
 * [695] 岛屿的最大面积
 *
 * https://leetcode-cn.com/problems/max-area-of-island/description/
 *
 * algorithms
 * Medium (64.32%)
 * Likes:    411
 * Dislikes: 0
 * Total Accepted:    70.5K
 * Total Submissions: 109.5K
 * Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
 *
 * 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
 * 
 * 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
 * 0（代表水）包围着。
 * 
 * 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
 * 
 * 
 * 
 * 示例 1:
 * 
 * [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 * ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
 * ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
 * ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
 * ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
 * ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
 * ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
 * ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
 * 
 * 
 * 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
 * 
 * 示例 2:
 * 
 * [[0,0,0,0,0,0,0,0]]
 * 
 * 对于上面这个给定的矩阵, 返回 0。
 * 
 * 
 * 
 * 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
 * 
 */

// @lc code=start
using System;

public class Solution
{
    int[][] grid;

    public int MaxAreaOfIsland(int[][] grid)
    {
        this.grid = grid;

        int nr = grid.GetLength(0);
        if (nr == 0)
            return 0;
        int nc = grid[0].GetLength(0);

        int res = 0;
        for (int i = 0; i < nr; i++)
            for (int j = 0; j < nc; j++)
                if (this.grid[i][j] == 1)
                    res = Math.Max(res, dfs(i, j, 1));
        return res;
    }

    private int dfs(int r, int c, int cnt)
    {
        grid[r][c] = 0;
        int[][] directions = new int[4][] { 
            new int[]{ r - 1, c }, 
            new int[]{ r + 1, c }, 
            new int[]{ r, c - 1 }, 
            new int[]{ r, c + 1 } };
        foreach (var direction in directions)
        {
            int x = direction[0], y = direction[1];
            if ((0 <= x && x < grid.GetLength(0) && (0 <= y && y < grid[x].GetLength(0))) && grid[x][y] == 1)
                cnt = dfs(x, y, cnt + 1);
        }
        return cnt;
    }
}
// @lc code=end

