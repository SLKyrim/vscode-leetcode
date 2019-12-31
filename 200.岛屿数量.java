/*
 * @lc app=leetcode.cn id=200 lang=java
 *
 * [200] 岛屿数量
 *
 * https://leetcode-cn.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (46.09%)
 * Likes:    317
 * Dislikes: 0
 * Total Accepted:    46.2K
 * Total Submissions: 99.6K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给定一个由 '1'（陆地）和
 * '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
 * 
 * 示例 1:
 * 
 * 输入:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * 输出: 1
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * 输出: 3
 * 
 * 
 */

// @lc code=start
import java.util.HashSet;

class UnionFind {
    private int[] roots;

    public UnionFind(int index) {
        roots = new int[index];
        for (int i = 0; i < index; i++) {
            roots[i] = i;
        }
    }

    private int findRoot(int index) {
        while (roots[index] != index) {
            roots[index] = roots[roots[index]];
            index = roots[index];
        }
        return index;
    }

    public void union(int index1, int index2) {
        int root1 = findRoot(index1);
        int root2 = findRoot(index2);
        if (root1 != root2) {
            roots[root1] = root2;
        }
    }

    public boolean isConnected(int index1, int index2) {
        return findRoot(index1) == findRoot(index2);
    }

    public int[] getRoots() {
        for (int i = 0; i < roots.length; i++) {
            // loop for make sure root connected
            roots[i] = findRoot(i);
        }
        return roots;
    }
}

class Solution {
    private int cols = 0;

    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }

        int rows = grid.length;
        cols = grid[0].length;

        UnionFind uf = new UnionFind(rows * cols + 1);
        int dummyNode = rows * cols;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '0') {
                    uf.union(xyTo1D(i, j), dummyNode);
                } else {
                    if (i - 1 >= 0 && grid[i - 1][j] == '1') {
                        uf.union(xyTo1D(i, j), xyTo1D(i - 1, j));
                    }
                    if (i + 1 < rows && grid[i + 1][j] == '1') {
                        uf.union(xyTo1D(i, j), xyTo1D(i + 1, j));
                    }
                    if (j - 1 >= 0 && grid[i][j - 1] == '1') {
                        uf.union(xyTo1D(i, j), xyTo1D(i, j - 1));
                    }
                    if (j + 1 < cols && grid[i][j + 1] == '1') {
                        uf.union(xyTo1D(i, j), xyTo1D(i, j + 1));
                    }
                }
            }
        }

        int[] roots = uf.getRoots();
        HashSet<Integer> res = new HashSet<>();
        for (int root : roots) {
            res.add(root);
        }
        return res.size() - 1;
    }

    private int xyTo1D(int row, int col) {
        return row * cols + col;
    }
}
// @lc code=end

