class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        
        #are they both equal?
        #do they have the same values?
        #do they have == 2 misplaced values 
        
        # if s1 == s2:
        #     return True
    
        if Counter(s1) != Counter(s2):
            return False 
        
        for i in range (len(s1)):
            if s1[i]!=s2[i]:
                c += 1
            if c>2:
                return False 
        return c <= 2
        
        
        
        