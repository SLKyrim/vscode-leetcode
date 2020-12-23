/*
 * @lc app=leetcode.cn id=387 lang=csharp
 *
 * [387] 字符串中的第一个唯一字符
 *
 * https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (47.54%)
 * Likes:    332
 * Dislikes: 0
 * Total Accepted:    139K
 * Total Submissions: 276.1K
 * Testcase Example:  '"leetcode"'
 *
 * 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
 * 
 * 
 * 
 * 示例：
 * 
 * s = "leetcode"
 * 返回 0
 * 
 * s = "loveleetcode"
 * 返回 2
 * 
 * 
 * 
 * 
 * 提示：你可以假定该字符串只包含小写字母。
 * 
 */

// @lc code=start
using System.Collections;

public class Solution
{
    public int FirstUniqChar(string s)
    {
        Hashtable tmp = new Hashtable();
        foreach (char ch in s)
        {
            if (!tmp.Contains(ch))
                tmp.Add(ch, 1);
            else
                tmp[ch] = (int)tmp[ch] + 1;
        }
        for (int i = 0; i < s.Length; ++i)
        {
            if ((int)tmp[s[i]] == 1)
                return i;
        }
        return -1;
    }
}

// @lc code=end

