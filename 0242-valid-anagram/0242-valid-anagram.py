class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if dic1.get(i) == None:
                dic1[i]=1
            else:
                dic1[i] += 1
        for i in t:
            if dic2.get(i) == None:
                dic2[i]=1
            else:
                dic2[i] += 1
        return dic1==dic2
                
        
        