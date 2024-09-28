class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:    

    def __init__(self, k: int):
        self.max = k
        self.count = 0
        self.L = Node(None)
        self.R = Node(None)
        self.L.right = self.R
        self.R.left = self.L

    def deleteNode(self, node):
        l,r = node.left, node.right
        l.right = r
        r.left = l
        self.count -= 1
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        first = self.L.right
        node = Node(value, self.L, first)
        self.L.right = node
        first.left = node

        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        last = self.R.left
        node = Node(value, last, self.R)
        self.R.left = node
        last.right = node

        self.count += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deleteNode(self.L.right)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deleteNode(self.R.left)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.L.right.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.R.left.val
        
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.max
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()