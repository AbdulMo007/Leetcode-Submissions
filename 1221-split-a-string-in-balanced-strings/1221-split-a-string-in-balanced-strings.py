class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        for i in s:
            if i=='R':
                r+=1
            elif i=='L':
                l+=1
            if l == r:
                count += 1
        return count
            
        