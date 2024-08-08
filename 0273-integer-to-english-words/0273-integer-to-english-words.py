class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = {
            "1" : "One",
            "2" : "Two",
            "3" : "Three",
            "4" : "Four",
            "5" : "Five",
            "6" : "Six",
            "7" : "Seven",
            "8" : "Eight",
            "9" : "Nine",
        }

        teens = {
            "10" : "Ten",
            "11" : "Eleven",
            "12" : "Twelve",
            "13" : "Thirteen",
            "14" : "Fourteen",
            "15" : "Fifteen",
            "16" : "Sixteen",
            "17" : "Seventeen",
            "18" : "Eighteen",
            "19" : "Nineteen",
        }

        tens = {
            "2" : "Twenty",
            "3" : "Thirty",
            "4" : "Forty",
            "5" : "Fifty",
            "6" : "Sixty",
            "7" : "Seventy",
            "8" : "Eighty",
            "9" : "Ninety",
        }

        def convertPart(s):
            res = []
            [a,b,c] = s
            # part 1 (hundreds)
            if a != "0":
                res.append(ones[a] + " Hundred")
            # part 2 (tens + ones)
            if b == "0":
                if c == "0":
                    pass
                else:
                    res.append(ones[c])
            elif b == "1":
                res.append(teens[b+c])
            else:
                if c != "0":
                    res.append(tens[b] + " " + ones[c])
                else:
                    res.append(tens[b])
                
            res = " ".join(res)
            # print(f"convertPart {s} -> {res}")
            return res
        
        parts = []
        part = ""
        while num > 0:
            c = num % 10
            # print(c)
            part = str(c) + part
            if len(part) == 3:
                parts.append(part)
                part = ""
            num //= 10
        if part != "":
            parts.append(part.zfill(3))
        
        # print(parts)

        # Thousand
        part_name = {
            1 : "Thousand",
            2 : "Million",
            3 : "Billion",
        }
        result = ""
        for i in range(len(parts)):
            if parts[i] == '000':
                continue
            if i > 0:
                result = convertPart(parts[i]) + " " + part_name[i] + " " + result
            else:
                result = convertPart(parts[i])
        
        return result.strip()