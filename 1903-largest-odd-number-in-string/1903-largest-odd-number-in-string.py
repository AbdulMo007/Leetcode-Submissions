class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while int(num[i]) % 2 == 0 and i>-1:
            i -= 1
        return num[:i+1]
        