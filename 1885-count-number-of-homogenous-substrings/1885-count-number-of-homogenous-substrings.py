class Solution:
    def countHomogenous(self, s: str) -> int:
        last_c = s[0]
        count = 0
        same_count = 1
        for c in s[1:]:
            if c != last_c:
                # print(f"same_count ={same_count} , {count} += {((same_count) / 2) * (1 + same_count)}")
                count += ((same_count) / 2) * (1 + same_count)
                same_count = 1
                last_c = c
            else:
                same_count += 1
        count += ((same_count) / 2) * (1 + same_count)

        return int(count) % (10 ** 9 + 7)