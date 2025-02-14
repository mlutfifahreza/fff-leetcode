class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.zero = -1

    def add(self, num: int) -> None:
        # print(f"add({num})")
        if not self.data:
            self.data.append(num)
            if num == 0: 
                self.zero = 0
        elif num == 0:
            self.zero = len(self.data)
            self.data.append(0)
        else:
            if self.data[-1] == 0:
                self.data.append(num)
            else:
                self.data.append(num * self.data[-1])

        # print(f"add num = {num} self.zero = {self.zero} self.data = {self.data}")
        
    def getProduct(self, k: int) -> int:
        # print(f"getProduct({k})")
        x = len(self.data) - k - 1
        if x < self.zero:
            # print(f"getProduct k={k} x={x} -> 0")
            return 0
        elif x == self.zero:
            return self.data[-1]
        else:
            # print(f"getProduct k={k} x={x} -> {self.data[-1] // self.data[x]}")
            return self.data[-1] // self.data[x]