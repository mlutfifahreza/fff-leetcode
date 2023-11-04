class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()

        while n != 1:
            if n in n_set:
                return False
            n_set.add(n)

            x = n
            new_n = 0
            while x > 0:
                new_n += (x%10)**2
                x //= 10
            print(f"new_n = {new_n}")
            n = new_n
        
        return True