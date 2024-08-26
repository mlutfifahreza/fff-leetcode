class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.right = self.tail
        self.tail.left = self.head

    def debug(self):
        cur = self.head
        s = []
        while cur:
            s.append(cur.val)
            cur = cur.right
        return s

    def remove(self, node):
        left, right = node.left, node.right
        left.right = right
        right.left = left

    def add_to_first(self, node):
        right = self.head.right
        self.head.right = node
        node.right = right
        node.left = self.head
        right.left = node

    def remove_lru(self):
        last = self.tail.left
        l,r = last.left, last.right
        l.right = r
        r.left = l
        return last

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add_to_first(node)
            return node.val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])

        node = Node(key, val)
        self.add_to_first(node)
        self.dic[key] = node
        if len(self.dic) > self.cap:
            removed = self.remove_lru()
            del self.dic[removed.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,val)