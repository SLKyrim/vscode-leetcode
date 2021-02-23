/*
 * @lc app=leetcode.cn id=130 lang=java
 *
 * [130] 被围绕的区域
 *
 * https://leetcode-cn.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (38.21%)
 * Likes:    129
 * Dislikes: 0
 * Total Accepted:    17.4K
 * Total Submissions: 45.1K
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
 * 
 * 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 * 
 * 示例:
 * 
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * 
 * 
 * 运行你的函数后，矩阵变为：
 * 
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 * 
 * 
 * 解释:
 * 
 * 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
 * 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
 * 
 */

// @lc code=start
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
}
class Solution {

    private int cols = 0;

    public void solve(char[][] board) {
        if (board.length == 0) {
            return;
        }

        int rows = board.length;
        cols = board[0].length;

        UnionFind uf = new UnionFind(rows * cols + 1);
        int dummyNode = rows * cols;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O') {
                    if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1) {
                        uf.union(xyTo1D(i, j), dummyNode);
                    } else {
                        if (i - 1 >= 0 && board[i - 1][j] == 'O') {
                            uf.union(xyTo1D(i, j), xyTo1D(i - 1, j));
                        }
                        if (i + 1 < rows && board[i + 1][j] == 'O') {
                            uf.union(xyTo1D(i, j), xyTo1D(i + 1, j));
                        }
                        if (j - 1 >= 0 && board[i][j - 1] == 'O') {
                            uf.union(xyTo1D(i, j), xyTo1D(i, j - 1));
                        }
                        if (j + 1 < cols && board[i][j + 1] == 'O') {
                            uf.union(xyTo1D(i, j), xyTo1D(i, j + 1));
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O' && !uf.isConnected(xyTo1D(i, j), dummyNode)) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    private int xyTo1D(int row, int col) {
        return row * cols + col;
    }
}
// @lc code=end

