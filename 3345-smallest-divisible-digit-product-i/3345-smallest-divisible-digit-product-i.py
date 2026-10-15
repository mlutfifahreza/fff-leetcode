class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr_num = n
        
        while True:
            product_digits = 1
            process_num = curr_num
            
            # Extract base-10 digits and calculate their product
            while process_num > 0:
                product_digits *= process_num % 10
                process_num //= 10
            
            # Check if product of digits is divisible by t
            if product_digits % t == 0:
                return curr_num
            
            curr_num += 1