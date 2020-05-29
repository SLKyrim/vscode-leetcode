#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (57.11%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    12.5K
# Total Submissions: 21.9K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n' +
  '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射
# 
# 具体地说，你的设计应该包含以下的功能
# 
# 
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
# 
# 
# 
# 示例：
# 
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1 
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到) 
# 
# 
# 
# 注意：
# 
# 
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。
# 
# 
#

# @lc code=start

class LList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = 2069
        self.hashMap = [None for _ in range(self.hash)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.hash # 取模得哈希值
        if not self.hashMap[index]:
            self.hashMap[index] = LList(key, value)
        else:
            # 【链式地址法】解决哈希冲突
            cur = self.hashMap[index]
            while True:
                if cur.key == key:
                    cur.val = value # key存在则更新值
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = LList(key, value) # 这里必须保证是cur.next，如果是等于None的cur，则链接不上


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.hash
        cur = self.hashMap[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.hash
        cur = pre = self.hashMap[index]
        if not cur:
            return
        if cur.key == key:
            self.hashMap[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    pre.next = cur.next
                    return
                cur = cur.next
                pre = pre.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

