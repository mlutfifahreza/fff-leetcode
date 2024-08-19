class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(nums, operands):
            # print(f"nums, operands {nums}, {operands}")
            val = nums[0]
            for i in range(len(operands)):
                if operands[i] == "+":
                    val += nums[i+1]
                else:
                    val -= nums[i+1]
            return val

        temp_num = ""
        nums = []
        operands = []
        
        digits = "1234567890"
        last_is_num = False
        for c in s:
            # print("c", c)
            if c in digits:
                if last_is_num:
                    temp_num += c
                else:
                    temp_num = c
                # print("temp_num", temp_num)
                last_is_num = True
            else:
                if c == ")":
                    if temp_num != "":
                        nums.append(int(temp_num))
                        temp_num = ""
                    temp_nums = [nums.pop()]
                    temp_ops = []
                    op = operands.pop()
                    while op != "(":
                        temp_nums = [nums.pop()] + temp_nums
                        temp_ops = [op] + temp_ops
                        op = operands.pop()
                    # print("temp_nums", temp_nums)
                    # print("temp_ops", temp_ops)
                    nums.append(evaluate(temp_nums, temp_ops))
                    # print("operands", operands)
                    # print("nums", nums)
                else:
                    if temp_num != "":
                        nums.append(int(temp_num))
                        temp_num = ""
                    if c != " ":
                        operands.append(c)
                    # print("operands", operands)
                    # print("nums", nums)
                last_is_num = False
            # print()
            
        
        if temp_num != "":
            nums.append(int(temp_num))
        
        # print("XX")
        # print("nums", nums)
        # print("operands", operands)

        return evaluate(nums, operands)