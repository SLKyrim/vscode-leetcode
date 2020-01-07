/*
 * @lc app=leetcode.cn id=212 lang=cpp
 *
 * [212] 单词搜索 II
 *
 * https://leetcode-cn.com/problems/word-search-ii/description/
 *
 * algorithms
 * Hard (37.78%)
 * Likes:    86
 * Dislikes: 0
 * Total Accepted:    7.8K
 * Total Submissions: 20.2K
 * Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
 *
 * 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
 * 
 * 
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
 * 
 * 示例:
 * 
 * 输入: 
 * words = ["oath","pea","eat","rain"] and board =
 * [
 * ⁠ ['o','a','a','n'],
 * ⁠ ['e','t','a','e'],
 * ⁠ ['i','h','k','r'],
 * ⁠ ['i','f','l','v']
 * ]
 * 
 * 输出: ["eat","oath"]
 * 
 * 说明:
 * 你可以假设所有输入都由小写字母 a-z 组成。
 * 
 * 提示:
 * 
 * 
 * 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
 * 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
 * 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Trie {
private:
    bool isEnd = false;
    Trie* nodes[26] = {nullptr};
    string word;

public:
    Trie() { }

    void insert(string word) {
        Trie* root = this;
        for (int i = 0; i < word.size(); i++) {
            if (root->nodes[word[i] - 'a'] == nullptr) {
                root->nodes[word[i] - 'a'] = new Trie();
            }
            root = root->nodes[word[i] - 'a'];
        }
        root->isEnd = true;
        root->word = word;
    }

    void search(vector<vector<char>>& board, vector<string>& res) {
        Trie* root = this;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                helper(res, board, root, i, j);
            }
        }
    }

    void helper(vector<string>& res, vector<vector<char>>& board, Trie* root, int i, int j) {
        if (root->isEnd) {
            root->isEnd = false;
            res.push_back(root->word);
            return;
        }

        if (0 <= i && i < board.size() && 0 <= j && j < board[0].size()) {
            if (board[i][j] != '#' && root->nodes[board[i][j] - 'a'] != nullptr) {
                Trie* currRoot = root->nodes[board[i][j] - 'a'];
                char tmp = board[i][j];
                board[i][j] = '#';
                helper(res, board, currRoot, i + 1, j);
                helper(res, board, currRoot, i - 1, j);
                helper(res, board, currRoot, i, j + 1);
                helper(res, board, currRoot, i, j - 1);
                board[i][j] = tmp;
            }
        }
    }
};

class Solution {
private:
    vector<string> res;
    Trie trie;

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        if (board.size() == 0 || words.size() == 0) {
            return res;
        }

        Trie* trie = new Trie();

        for (string word : words) {
            trie->insert(word);
        }

        trie->search(board, res);

        return res;
    }
};
// @lc code=end

