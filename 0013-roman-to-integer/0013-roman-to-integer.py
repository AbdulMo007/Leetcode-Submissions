class Solution:
    def romanToInt(self, s: str) -> int:
        
        D = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        
        sum = D[s[-1]]
        
        for i in range (len(s)-1, 0, -1):
            if D[s[i-1]]<D[s[i]]:
                sum = sum-D[s[i-1]]
            else:
                sum += D[s[i-1]]
        return sum
        
        
        
        