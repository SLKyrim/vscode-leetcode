#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.81%)
# Likes:    433
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 79.4K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

# @lc code=start
class DLList:
    def __init__(self, key = 0, val = 0):
        self.key = key # 在删除哈希表中的节点时用到
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = dict() # 哈希表存key-节点对
        # 使用伪头伪尾，添加和删除节点时不需检查相邻节点是否存在
        self.dummyHead = DLList()
        self.dummyTail = DLList()
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            node = DLList(key, value) # 如果key不存在，创建一个新节点
            self.table[key] = node # 添加进哈希表
            self.addToHead(node) # 添加至双向链表头部
            self.size += 1
            if self.size > self.capacity:
                removeNode = self.removeTail() # 超过容量，去除尾部节点
                self.table.pop(removeNode.key) # 按key去掉哈希表中对应节点
                self.size -= 1
        else:
            node = self.table[key] # key存在，从哈希表中取出
            node.val = value # 更改节点的值
            self.moveToHead(node) # 将节点移到头部

    def moveToHead(self, node):
        """将节点node移到链表头部"""
        self.remove(node) # 先删除节点
        self.addToHead(node) # 再将节点添加到头部

    def remove(self, node):
        """将节点node删除"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeTail(self):
        """将链表尾部删除"""
        node = self.dummyTail.prev
        self.remove(node)
        return node # 返回删除节点是方便在哈希表中用它的key删除它

    def addToHead(self, node):
        """将节点node添加到链表头"""
        node.prev = self.dummyHead
        node.next = self.dummyHead.next
        self.dummyHead.next.prev = node
        self.dummyHead.next = node

# 用封装好的数据结构OrderedDict面试直接给挂
# from collections import OrderedDict

# class LRUCache(OrderedDict):
#     # 继承有序字典的属性，有序字典按加入键值得顺序排序
#     def __init__(self, capacity: int):
#       self.capacity = capacity

#     def get(self, key: int) -> int:
#       if key not in self:
#         return -1
#       self.move_to_end(key) # 将key为键的键值对放到字典最后
#       return self[key]

#     def put(self, key: int, value: int) -> None:
#       if key in self:
#         self.move_to_end(key) # 若新加的键已在字典中，则把该键提到最后再更新其值
#       self[key] = value
#       if len(self) > self.capacity:
#         self.popitem(last=False) # last=False删掉最先的键值对，否则popitem()默认删掉最后加入的键值对

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

