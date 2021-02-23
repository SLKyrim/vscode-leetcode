/*
 * @lc app=leetcode.cn id=383 lang=java
 *
 * [383] 赎金信
 *
 * https://leetcode-cn.com/problems/ransom-note/description/
 *
 * algorithms
 * Easy (50.66%)
 * Likes:    62
 * Dislikes: 0
 * Total Accepted:    13.9K
 * Total Submissions: 27.1K
 * Testcase Example:  '"a"\n"b"'
 *
 * 给定一个赎金信 (ransom)
 * 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回
 * true ；否则返回 false。
 * 
 * (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
 * 
 * 注意：
 * 
 * 你可以假设两个字符串均只含有小写字母。
 * 
 * 
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 * 
 * 
 */

// @lc code=start
import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] arr = magazine.toCharArray();
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : arr) {
            if (!map.containsKey(c)) {
                map.put(c, 1);
            } else {
                map.put(c, map.get(c) + 1);
            }
        }

        char[] arr2 = ransomNote.toCharArray();
        for (char c : arr2) {
            if (!map.containsKey(c)) {
                return false;
            } else {
                if (map.get(c) == 0) {
                    return false;
                } else {
                    map.put(c, map.get(c) - 1);
                }
            }
        }
        return true;
    }
}
// @lc code=end

