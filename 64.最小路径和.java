/*
 * @lc app=leetcode.cn id=64 lang=java
 *
 * [64] 最小路径和
 *
 * https://leetcode-cn.com/problems/minimum-path-sum/description/
 *
 * algorithms
 * Medium (63.12%)
 * Likes:    351
 * Dislikes: 0
 * Total Accepted:    48.7K
 * Total Submissions: 76.6K
 * Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
 *
 * 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
 * 
 * 说明：每次只能向下或者向右移动一步。
 * 
 * 示例:
 * 
 * 输入:
 * [
 * [1,3,1],
 * ⁠ [1,5,1],
 * ⁠ [4,2,1]
 * ]
 * 输出: 7
 * 解释: 因为路径 1→3→1→1→1 的总和最小。
 * 
 * 
 */

// @lc code=start
import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {

    public int minPathSum(int[][] grid) {

        int rowBound = grid.length;
        int colBound = grid[0].length;
        
        class SearchNode implements Comparable<SearchNode> {
            private int priority;
            private int row;
            private int col;
            
            public SearchNode(int i, int j) {
                priority = Integer.MAX_VALUE;
                row = i;
                col = j;
            }

            public SearchNode(int distance, int i, int j) {
                priority = distance;
                row = i;
                col = j;
            }

            public int getDist() {
                return priority;
            }

            public String[] neighbors() {
                String[] res = new String[2];
                if (row + 1 < rowBound) {
                    res[0] = (row + 1) + " " + col;
                }
                if (col + 1 < colBound) {
                    res[1] = row + " " + (col + 1); 
                }
                return res;
            }

            @Override
            public int compareTo(SearchNode o) {
                return this.priority - o.priority;
            }
        }

        PriorityQueue<SearchNode> pq = new PriorityQueue<>();
        HashMap<String, SearchNode> map = new HashMap<>();

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (i == 0 && j == 0) {
                    map.put(i + " " + j, new SearchNode(grid[i][j], i, j));
                    pq.add(map.get(i + " " + j));
                } else {
                    map.put(i + " " + j, new SearchNode(i, j));
                    pq.add(map.get(i + " " + j));
                }
            }
        }

        boolean isReached = false;

        while (!isReached && !pq.isEmpty()) {
            SearchNode curr = pq.remove();
            for (String n : curr.neighbors()) {
                if (n != null) {
                    String[] id = n.split("\\s+");
                    int nRow = Integer.parseInt(id[0]);
                    int nCol = Integer.parseInt(id[1]);
                    int currDist = curr.getDist() + grid[nRow][nCol];
                    if (map.get(n).getDist() > currDist) {
                        pq.remove(map.get(n));
                        map.replace(n, new SearchNode(currDist, nRow, nCol));
                        pq.add(map.get(n));
                    }

                    if (nRow == rowBound - 1 && nCol == colBound - 1) {
                        isReached = true;
                    }
                }
            }
        }

        return map.get((rowBound - 1) + " " + (colBound - 1)).getDist();
        
    }
}
// @lc code=end

