class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = [nums[0]]
        a2 = [nums[1]]

        a,b = a1[0], a2[0]

        for i in range(2, len(nums)):
            ni = nums[i]
            if a > b:
                a1.append(ni)
                a = ni
            else:
                a2.append(ni)
                b = ni
        
        return a1 + a2