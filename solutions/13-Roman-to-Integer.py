class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")         # 4
        s = s.replace("IX", "IIIIIIIII")    # 9
        s = s.replace("XL", "XXXX")         # 40
        s = s.replace("XC", "XXXXXXXXX")    # 90
        s = s.replace("CD", "CCCC")         # 400
        s = s.replace("CM", "CCCCCCCCC")    # 900

        sum = 0

        for ch in s:
            if ch == "I":
                sum += 1
            elif ch == "V":
                sum += 5
            elif ch == "X":
                sum += 10
            elif ch == "L":
                sum += 50
            elif ch == "C":
                sum += 100
            elif ch == "D":
                sum += 500
            elif ch == "M":
                sum += 1000

        return sum


p1 = Solution()
print(p1.romanToInt("III"))         # Expected output: 3
print(p1.romanToInt("LVIII"))       # Expected output: 58
print(p1.romanToInt("MCMXCIV"))     # Expected output: 1994