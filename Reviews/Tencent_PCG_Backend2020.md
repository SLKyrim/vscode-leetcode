# TencentPCG2020 后端开发笔试
## 目录
* [电话号码格式](#电话号码格式)
* [房屋涂色](#房屋涂色)
* [差异最小的环形队列](#差异最小的环形队列)
* [最少的上漆次数](#最少的上漆次数)
* [指令序列可达的最远距离](#指令序列可达的最远距离)
* [总结](#总结)

## 电话号码格式

合法的电话号码格式是11位且第一个数必须是8。  
对每一个输入的数字号码字符串，判断是否能经过删除0个或若干个数字变成合法的电话号码，如果可以合法输出YES，否则输出NO

**输入描述**：   
第一行一个整数t表示测试用例的组数
接下来2*t行，每个测试用例包含2行，第1行一个整数n表示字符串的长度，第2行一个字符串s    
输入满足1<=t<=100, 1<=n<=100,每个字符串只包含数字

### 示例

>输入：   
    2   
    11   
    88888888888  
    3   
    000   
输出：   
    YES   
    NO
 
### 思路1

首先获取输入字串长度n，n小于11必不合法。    
然后用find()查找输入字串的第1个“8”的位置，如果没有8则比不合法。    
第一个8前面的数都要删掉从而保证第一个数字是8，判断删掉前面的数字后剩余的字串长度仍大于等于11则可以经过删除操作变成合法号码。

### 代码1

```Python
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    e = s.find("8")
    if n < 11 or e == -1:
        print("NO")
        continue
    if n - e >= 11:
        print("YES")
    else:
        print("NO")
```

## 房屋涂色

[Leetcode 256 粉刷房子](https://leetcode-cn.com/problems/paint-house/)    
n栋房屋需要粉刷，有红绿蓝三种颜色，相邻房屋粉刷颜色需要不一样，且用一种颜色粉刷不同房屋时花费也不一定一样，如粉刷第i栋房屋，刷成红色花费r[i]，绿色花费g[i]，蓝色花费b[i]。    
问刷这n栋房屋需要的最小花费。

**输入描述**：   
第一行一个整数n（1<=n<=20）表示需要粉刷的房屋数   
接下来n行，每行三个整数分别表示粉刷房屋成红色，绿色，蓝色需要的费用

### 示例

>输入：   
4   
100 77 73   
41 74 83    
9 91 93      
50 16 31     
输出：    
172

### 思路1

一道简单的DP题，dp[i][j]表示已粉刷了前i-1栋房屋，第i栋房屋粉刷成j色时的最小花费。
状态转移方程为：    
dp[i][red] = min(dp[i-1][green], dp[i-1][blue]) + cost[red]    
dp[i][green] = min(dp[i-1][red], dp[i-1][blue]) + cost[green]    
dp[i][blue] = min(dp[i-1][green], dp[i-1][red]) + cost[blue]    

### 代码1

```Python
n = int(input())
dp = [[0] * 3 for _ in range(n)]
cost = [int(x) for x in input().split()]
dp[0][0] = cost[0]
dp[0][1] = cost[1]
dp[0][2] = cost[2]
for i in range(1, n):
    cost = [int(x) for x in input().split()]
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cost[2]
print(min(dp[-1]))
```

## 差异最小的环形队列

n个人手拉手排成一个圆圈，每个人身高不同，求使圆圈中相邻人身高最大差异最小的排序。

**输入描述**：    
第一行一个整数n(2<=n<100)表示人数    
第二行n个数字表示每个人的身高，范围在[1, 10^9]之间

### 示例

>输入：   
5    
2 1 1 3 2    
输出：    
1 2 3 2 1

### 思路1

先对身高排序，然后按顺序依次取身高轮流放在队列前面和后面。

### 代码1

```Python
n = int(input())
nums = [int(x) for x in input().split()]
left, right = list(), list()
nums.sort()
for i in range(n):
    if i % 2 == 0:
        left.append(str(nums[i]))
    else:
        right.insert(0, str(nums[i]))
print(" ".join(left + right))
```

## 最少的上漆次数

给n根宽为1，高度为$A_i$的木板。模板竖起来并排排成一排。    
每次上漆只能连续横刷或竖刷宽度为1的范围。求刷完所有模板的最少上漆次数。

**输入描述**：    
第一行一个整数n表示木板数量（1<=n<=5000）    
第二行n个数表示木板的高度，范围在[1, 1e9]内

### 示例

>输入：    
5    
2 2 1 2 2    
输出：    
3   
解释：   
第1次上漆，横着涂高度为1的下面5 * 1的面积     
第2次上漆，横着涂高度为2的左边2 * 1的面积    
第3次上漆，横着涂高度为2的右边2 * 1的面积

### 思路1

核心思路是：对每个高度，判断可以横着涂的范围数，如果范围间隔只有1，则竖着涂好这个木板，横着涂的次数即间隔大于1的范围数。用一个集合记录已经涂好的木板索引用来确认横着涂的范围。    
但是高度范围[1, 1e9]较大，逐个高度的检查会超时，而木板数量最高只有5000，所以对高度超过5000的木板直接竖着先涂好从而避免超时。

### 代码1

```Python
n = int(input())
nums = [int(x) for x in input().split()]
res = 0
fin = set() # 记录已完成涂色的木板索引
for i in range(n):
    if nums[i] > 5000:
        fin.add(i) # 高度超过给定最多木板个数的木板直接竖着涂好
        res += 1
# 对高度在给定最多木板个数内的木板进行上漆
for h in range(1, 5001):
    if len(fin) == n:
        break # 所有木板已上好漆
    tmp = [-1] # 记录当前高度上已上好漆的木板索引
    for i in range(n):
        if i in fin:
            tmp.append(i)
            continue
        if nums[i] < h:
            fin.add(i)
            tmp.append(i)
    tmp.append(n)
    row = [] # 记录上好漆的木板之间的间隔
    for i in range(1, len(tmp)):
        cur = tmp[i] - tmp[i-1] - 1
        if cur == 1:
            res += 1 # 间隔为1则直接把中间这块木板竖着涂满  
            fin.add((tmp[i] + tmp[i-1]) // 2) 
        elif cur == 0:
            continue
        else:
            row.append(cur) # 间隔超过1则横着涂满这一高度的间隔范围
            for j in range(tmp[i-1]+1, tmp[i]):
                if nums[j] == h:
                    fin.add(j) # 添加已在当前高度上漆完成的木板索引
    res += len(row) # 有多少个间隔大于1的区域，就要横着上漆多少次

print(res)
```

## 指令序列可达的最远距离

[Codeforces 132C](http://codeforces.com/problemset/problem/132/C)

有一个由T和F组成的控制指令，T表示转向，F表示向前一步。对给定的指令序列需要修改n次，每次修改是把T改为F或者F改为T。求修改指令后可以到达的最远距离。

**输入描述**：    
第一行是一个由F和T组成的字符串，长度<=100       
第二行一个整数n（1<=n<=50）表示修改次数

### 示例

>输入：     
FFT     
1     
输出：     
3    
解释：   
把最后的T修改为F，则可以向前走3步    

### 思路1

三维DP。    

需要先用最远距离无法小于的小数给dp数组赋值保证答案正确。

dp[i][j][d]表示由前i个指令组成的序列，在第i个指令修改j次后，往方向d能到达的最远距离。        
当line[i] == "F"时，若在第i个指令上修改的次数k为奇数，则line[i]会被修改为“T”，因此只改变方向；同理当line[i] == "T"时，若在第i个指令上修改的次数k为偶数，则line[i]保持为“T"不变，也仅只改变方向，此时有状态转移方程：     
dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-k][1])     
dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-k][0])

当line[i] == "F"时，若在第i个指令上修改的次数k为偶数，则line[i]会被保持为“F”不变，在原来的方向上往前迈一步；当line[i] == "T"时，若在第i个指令上修改的次数k为奇数，则line[i]修改为“F”，需要在原来的方向上往前迈一步，此时状态转移方程为：     
dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-k][0] + 1)     
dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-k][1] - 1)

### 代码1

```Python
line = input()
n = int(input())
dp = [[[-100] * 2 for _ in range(n+1)] for _ in range(len(line)+1)]
dp[0][0][0], dp[0][0][1] = 0, 0
for i in range(1, len(line)+1):
    for j in range(n+1):
        for k in range(j+1):
            if (line[i-1] == "F" and k % 2 == 1) or (line[i-1] == "T" and k % 2 == 0):
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-k][1])
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-k][0])
            else:
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-k][0] + 1)
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-k][1] - 1)
print(max(dp[-1][-1][0], dp[-1][-1][1]))
```

## 总结

AK      
和一年前秋招时做T家笔试时只能AC两道比确实有了很大的进步，说明Leetcode的周赛确实还是很能锻炼人的。      
1、简单的字符串删除操作模拟题，忘了考虑find()不出8的情况，WA了1次40%    
2、粉刷房子，简单的二维DP，leetcode经典原题    
3、模拟题，没把握答案正确（因为没有数学验证）的思路AC了   
4、比较复杂的模拟题，TLE了1次，利用输入数据的范围竖涂了一些高度很高的木板，然后就AC了     
5、非常难的三维DP，很抽象，不过好在是CodeForces的原题。不过笔试完我Run了下CF上的用例没通过，修改了dp的初始赋值才通过，所以笔试时是运气好AC了这一题。     
看了下NowCoder上的帖子，五月份的题目也用的这一套，感觉有点随意了...

