/*
 * @lc app=leetcode.cn id=208 lang=java
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
/** Easy Understand Solution */
// class Trie {

//     private static final int R = 26;

//     private class Node {
//         boolean isEnd;
//         Node[] links;

//         public Node() {
//             links = new Node[R];
//             isEnd = false;
//         }

//         public boolean containsKey(char ch) {
//             return links[ch - 'a'] != null;
//         }

//         public void put(char ch, Node node) {
//             links[ch - 'a'] = node;
//         }

//         public Node get(char ch) {
//             return links[ch - 'a'];
//         }

//         public void setEnd() {
//             isEnd = true;
//         }

//         public boolean getEnd() {
//             return isEnd;
//         }
//     }

//     private Node root;

//     /** Initialize your data structure here. */
//     public Trie() {
//         root = new Node();
//     }
    
//     /** Inserts a word into the trie. */
//     public void insert(String word) {
//         Node node = root;
//         for (int i = 0; i < word.length(); i++) {
//             char currChar = word.charAt(i);
//             if (!node.containsKey(currChar)) {
//                 node.put(currChar, new Node() );
//             }
//             node = node.get(currChar);
//         }
//         node.setEnd();
//     }
    
//     /** Returns if the word is in the trie. */
//     public boolean search(String word) {
//         Node node = root;
//         for (int i = 0; i < word.length(); i++) {
//             if (node.containsKey(word.charAt(i))) {
//                 node = node.get(word.charAt(i));
//             } else {
//                 return false;
//             }
//         }
//         if (!node.getEnd()) {
//             return false;
//         }
//         return true;
//     }
    
//     /** Returns if there is any word in the trie that starts with the given prefix. */
//     public boolean startsWith(String prefix) {
//         Node node = root;
//         for (int i = 0; i < prefix.length(); i++) {
//             if (node.containsKey(prefix.charAt(i))) {
//                 node = node.get(prefix.charAt(i));
//             } else {
//                 return false;
//             }
//         }
//         return true;
//     }
// }

/** Less Code (simplify) Solution */
class Trie {
    private final int R = 26;
    private boolean isEnd = false;
    private Trie[] nodes; 

    public Trie() {
        nodes = new Trie[R]; 
    }

    public void insert(String word) {
        Trie root = this;
        for (int i = 0; i < word.length(); i++) {
            if (root.nodes[word.charAt(i) - 'a'] == null) {
                root.nodes[word.charAt(i) - 'a'] = new Trie();
            }
            root = root.nodes[word.charAt(i) - 'a'];
        }
        root.isEnd = true;
    }

    public boolean search(String word) {
        Trie root = this;
        for (int i = 0; i < word.length(); i++) {
            if (root.nodes[word.charAt(i) - 'a'] == null) {
                return false;
            }
            root = root.nodes[word.charAt(i) - 'a'];
        }
        return root.isEnd;
    }

    public boolean startsWith(String prefix) {
        Trie root = this;
        for (int i = 0; i < prefix.length(); i++) {
            if (root.nodes[prefix.charAt(i) - 'a'] == null) {
                return false;
            }
            root = root.nodes[prefix.charAt(i) - 'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
// @lc code=end

