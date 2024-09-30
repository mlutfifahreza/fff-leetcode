class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.L = Node(0)
        self.R = Node(0)
        self.L.r = self.R
        self.R.l = self.L

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return

        last = self.R.l
        new_node = Node(x, last, self.R)
        last.r = new_node
        self.R.l = new_node
        self.size += 1
        # self.debug("PUSH")
        

    def pop(self) -> int:
        if self.size == 0:
            return -1

        a,b,c = self.R.l.l , self.R.l , self.R

        a.r = c
        c.l = a

        self.size -= 1
        # self.debug("POP")
        return b.val
        

    def increment(self, k: int, val: int) -> None:
        node = self.L.r
        while node and k:
            node.val = node.val + val
            node = node.r
            k -= 1
        # self.debug("INC")

    def debug(self, msg):
        node = self.L.r
        res = []
        while node.r:
            res.append(node.val)
            node = node.r
        print(msg, res)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)