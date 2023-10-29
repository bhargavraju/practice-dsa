"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if
the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
If the key is already present, update the value

When the cache reaches its capacity, it should invalidate the least recently
used item before inserting the new item.
The LRUCache will be initialized with an integer corresponding to its capacity.
Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of "least recently used" : An access to an item is defined as
a get or a set operation of the item. "Least recently used" item is the one
with the oldest access time.

NOTE: If you are using any global variables, make sure to clear them in the
constructor.

Example :

Input :
         capacity = 2
         set(1, 10)
         set(5, 12)
         get(5)        returns 12
         get(1)        returns 10
         get(10)       returns -1
         set(6, 14)    this pushes out key = 5 as LRU is full.
         get(5)        returns -1
"""


class DLLNode:

    def __init__(self, val, key=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
    node.prev = None
    node.next = None
    return node


def append_node(node, tail):
    prev_node = tail.prev
    prev_node.next = node
    node.prev = prev_node
    tail.prev = node
    node.next = tail
    return node


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dll_head = DLLNode(0)
        self.dll_tail = DLLNode(0)
        self.dll_head.next = self.dll_tail
        self.dll_tail.prev = self.dll_head
        self.store = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self.store:
            return -1
        node = self.store[key]
        delete_node(node)
        append_node(node, self.dll_tail)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.store:
            node = self.store[key]
            delete_node(node)
        node = DLLNode(value, key)
        self.store[key] = node
        append_node(node, self.dll_tail)
        if len(self.store) > self.capacity:
            least_node = delete_node(self.dll_head.next)
            self.store.pop(least_node.key)


cache = LRUCache(1)
print('step 1')
cache.set(2, 1)
print('step 2')
cache.set(2, 2)
print('step 3')
cache.get(2)
print('step 3')
cache.set(1, 1)
print('step 4')
cache.set(4, 1)
print('step 5')
cache.get(2)