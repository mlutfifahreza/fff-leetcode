class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        counter = 0

        # Process each bit from least significant to most significant
        while num > 0:
            # Extract the current least significant bit
            temp = num & 1

            # If the bit is 0, set the corresponding bit in the result
            if temp == 0:
                res += pow(2, counter)

            # Shift right to process the next bit
            num = num >> 1

            # Move to the next bit position
            counter += 1

        return res