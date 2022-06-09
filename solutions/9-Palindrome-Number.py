class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        spl = int(len(xStr) / 2)

        if len(xStr) % 2 == 0:  # even
            return xStr[:spl] == (xStr[spl:])[::-1]
        else:  # odd
            return xStr[:spl] == (xStr[spl + 1:])[::-1]


p1 = Solution()
print(p1.isPalindrome(121))     # Expected output: True
print(p1.isPalindrome(-121))    # Expected output: False
print(p1.isPalindrome(10))      # Expected output: False
print(p1.isPalindrome(13531))   # Expected output: True