class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1 = [None]*(len(s))
        j = 0
        for i in (s):
            s1[indices[j]] = i
            j += 1
        return "".join(s1)
        
        