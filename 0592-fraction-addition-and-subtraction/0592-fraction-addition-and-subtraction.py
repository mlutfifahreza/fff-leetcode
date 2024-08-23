class Solution:
    def fractionAddition(self, expression: str) -> str:
        signs = []
        nums = []
        denums = []

        cur_num = 0
        if expression[0] not in "+-":
            expression = "+" + expression

        for c in expression:
            if c in "+-":
                signs.append(c)
                denums.append(cur_num)
                cur_num = 0
            elif c == "/":
                nums.append(cur_num)
                cur_num = 0
            else:
                cur_num = cur_num*10 + int(c)
        denums.append(cur_num)
        denums = denums[1:]

        for i in range(len(signs)):
            if signs[i] == "-":
                nums[i] = -nums[i]
        
        # print(signs)
        # print(nums)
        # print(denums)

        common_num = 1
        for d in denums:
            common_num *= d
        # print(common_num)

        num_sum = 0
        for i in range(len(nums)):
            num_sum += nums[i] * (common_num//denums[i])
            # print(num_sum)
        # print("num_sum ",  num_sum)

        for i in range(2, common_num+1):
            # print("i", i)
            while num_sum%i == 0 and common_num%i == 0:
                # print("i", True)
                num_sum //= i
                common_num //= i
                # print("->", num_sum)
                # print("->", common_num)

        # print(num_sum)
        # print(common_num)

        return f"{num_sum}/{common_num}"