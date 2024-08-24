class Solution:
    def nearestPalindromic(self, n: str) -> str:
        s = n
        n = int(s)
        w = len(s)
        is_odd = w % 2 == 1

        mid = ""
        mid_i = (w-1) // 2
        if is_odd:
            mid = s[mid_i]
        
        # match left right
        # print("mid_i", mid_i)
        if is_odd:
            left = s[0:mid_i]
        else:
            left = s[0:mid_i+1]

        if mid_i == 0 and left == '':
            return f'{n-1}'

        # print("left", left)
        # print("mid", mid)

        def rev(s):
            res = ''
            for c in s:
                res = c + res
            return res

        def is_pol(s):
            i,j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    # print(f"is_pol({s}) false")
                    return False
                i += 1
                j -= 1
            # print(f"is_pol({s}) true")
            return True

        pol_list = []
        
        change_digit_low = ''
        for _ in range(w-1):
            change_digit_low += '9'
        if is_pol(change_digit_low):
            pol_list.append(int(change_digit_low))
        # print("change_digit_low", change_digit_low)

        change_digit_high = '1'
        for _ in range(w-1):
            change_digit_high += '0'
        change_digit_high += '1'
        if is_pol(change_digit_high):
            pol_list.append(int(change_digit_high))
        # print("change_digit_high", change_digit_high)
        

        for v in [int(left) - 1, int(left), int(left) + 1]:
            v_rev = rev(str(v))
            if is_odd:
                for m in [int(mid)-1, int(mid), int(mid)+1]:
                    if 0 <= m <= 9:
                        new_v = f'{v}{m}{v_rev}'
                        if new_v != s:
                            pol_list.append(new_v)
            else:
                new_v = f'{v}{v_rev}'
                if new_v != s:
                    pol_list.append(new_v)
        
        # print(pol_list)

        dist_pols = {}
        for v in pol_list:
            d = abs(n - int(v))
            if d not in dist_pols:
                dist_pols[d] = []
            dist_pols[d].append(int(v))

        # print("dist_pols", dist_pols)
        min_dist = min(dist_pols)
        res = min(dist_pols[min_dist])
        return str(res)