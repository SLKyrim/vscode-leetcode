/*
 * @lc app=leetcode.cn id=79 lang=cpp
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (39.40%)
 * Likes:    273
 * Dislikes: 0
 * Total Accepted:    30.2K
 * Total Submissions: 76.2K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 * 
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 * 
 * 示例:
 * 
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 * 
 * 给定 word = "ABCCED", 返回 true.
 * 给定 word = "SEE", 返回 true.
 * 给定 word = "ABCB", 返回 false.
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> visited;
    int correctLen = 0;

    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();

        visited = vector<vector<int>>(rows, vector<int>(cols, 0));

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (helper(board, rows, cols, word, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    bool helper(vector<vector<char>>& board, int rows, int cols, string word, int i, int j) {
        if (correctLen == word.size()) {
            return true;
        }

        bool res = false;

        if (0 <= i && i < rows && 0 <= j && j < cols && visited[i][j] == 0 && board[i][j] == word[correctLen]) {
            correctLen += 1;
            visited[i][j] = 1;
            res = helper(board, rows, cols, word, i - 1, j) || 
                  helper(board, rows, cols, word, i + 1, j) || 
                  helper(board, rows, cols, word, i, j - 1) || 
                  helper(board, rows, cols, word, i, j + 1);
            if (res == false) {
                correctLen -= 1;
                visited[i][j] = 0;
            }
        }

        return res;
    }
};
// @lc code=end

