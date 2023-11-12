class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,1
        num_len = len(numbers)
        while 1:
            a,b = numbers[l], numbers[r]
            add = a + b
            if add > target:
                while numbers[l] == a:  
                    l += 1
                r = l + 1
            elif add == target:
                return [l+1, r+1]
            else:
                while r < num_len and numbers[r] == b:
                    r += 1
                if r == num_len:
                    while numbers[l] == a:
                        l += 1
                    r = l + 1