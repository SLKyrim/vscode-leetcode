/*
 * @lc app=leetcode.cn id=204 lang=cpp
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (30.94%)
 * Likes:    223
 * Dislikes: 0
 * Total Accepted:    32.8K
 * Total Submissions: 105.7K
 * Testcase Example:  '10'
 *
 * 统计所有小于非负整数 n 的质数的数量。
 * 
 * 示例:
 * 
 * 输入: 10
 * 输出: 4
 * 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        // 厄拉多塞筛法
        if (n <= 1) return 0;
        vector<int> tmp(n, 1);
        tmp[0] = 0, tmp[1] = 0;
        // 在sqrt(n)内可以检查所有质数的倍数
        // 证明： 若n可以因数分解，即n = p * q， 因为p <= q, 所以p <= sqrt(n)
        // 所以可以在sqrt(n)内标记n内所有的非质数
        for (int i = 2; i <= sqrt(n); i++) { 
            if (tmp[i] == 1) {
                for (int j = i*i; j < n; j += i) {
                    tmp[j] = 0; // 将质数的倍数置为0
                }
            }
        }
        return count(tmp.begin(), tmp.end(), 1);
        
        // // 常规判断素数超时
        // if (n <= 1) return 0;
        // int cnt = 0;    
        // for (int i = 2; i < n; i++) {
        //     // 判断素数
        //     bool isPrime = true;
        //     for (int j = 2; j <= i/2; j++) {
        //         if (i % j == 0) {
        //             isPrime = false;
        //             break;
        //         }
        //     }
        //     if (isPrime) cnt += 1;
        // }
        // return cnt;
    }
};
// @lc code=end

