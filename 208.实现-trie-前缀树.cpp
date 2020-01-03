/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 *
 * https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (62.69%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    19.6K
 * Total Submissions: 30.9K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
 * 
 * 示例:
 * 
 * Trie trie = new Trie();
 * 
 * trie.insert("apple");
 * trie.search("apple");   // 返回 true
 * trie.search("app");     // 返回 false
 * trie.startsWith("app"); // 返回 true
 * trie.insert("app");   
 * trie.search("app");     // 返回 true
 * 
 * 说明:
 * 
 * 
 * 你可以假设所有的输入都是由小写字母 a-z 构成的。
 * 保证所有输入均为非空字符串。
 * 
 * 
 */

// @lc code=start
#include <map>
using namespace std;

class Trie {
private:
    class Node {
    private:
        int R = 26;
        map<int, Node*> links;
        bool isEnd;
    public:
        Node() {
            isEnd = false;
        }

        bool containsKey(char ch) {
            return links.count(ch - 'a') != 0;
        }

        void put(char ch, Node* node) {
            links.insert(pair<int, Node*>(ch - 'a', node));
        }

        Node* get(char ch) {
            return links[ch - 'a'];
        }

        void setEnd() {
            isEnd = true;
        }

        bool getEnd() {
            return isEnd;
        }
    };

    Node* root;

public:
    /** Initialize your data structure here. */
    Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node* node = root;
        for (int i = 0; i < word.size(); i++) {
            char currChar = word[i];
            if (!(*node).containsKey(currChar)) {
                (*node).put(currChar, new Node());
            }
            node = (*node).get(currChar);
        }
        (*node).setEnd();
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node* node = root;
        for (int i = 0; i < word.size(); i++) {
            if ((*node).containsKey(word[i])) {
                node = (*node).get(word[i]);
            }
            else {
                return false;
            }
        }
        if (!(*node).getEnd()) {
            return false;
        }
        return true;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Node* node = root;
        for (int i = 0; i < prefix.size(); i++) {
            if ((*node).containsKey(prefix[i])) {
                node = (*node).get(prefix[i]);
            }
            else {
                return false;
            }
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

