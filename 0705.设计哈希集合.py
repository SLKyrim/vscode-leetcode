#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (56.43%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 24.6K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合
# 
# 具体地说，你的设计应该包含以下的功能
# 
# 
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 
# 
# 
# 示例:
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // 返回 true
# hashSet.contains(3);    // 返回 false (未找到)
# hashSet.add(2);          
# hashSet.contains(2);    // 返回 true
# hashSet.remove(2);          
# hashSet.contains(2);    // 返回  false (已经被删除)
# 
# 
# 
# 注意：
# 
# 
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。
# 
# 
#

# @lc code=start
class LList:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = 2069
        self.hashSet = [None for _ in range(self.hash)]

    def add(self, key: int) -> None:
        index = key % self.hash # 取模得哈希值
        if not self.hashSet[index]:
            self.hashSet[index] = LList(key)
        else:
            # 【链式地址法】解决哈希冲突
            cur = self.hashSet[index]
            while True:
                if cur.key == key:
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = LList(key)

    def remove(self, key: int) -> None:
        index = key % self.hash
        cur = pre = self.hashSet[index]
        if not cur:
            return
        if cur.key == key:
            self.hashSet[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    pre.next = cur.next
                    return
                cur = cur.next
                pre = pre.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.hash
        cur = self.hashSet[index]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

