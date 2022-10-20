class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(indices)
        for i in range(len(indices)):
            ans[indices[i]] = s[i]
        return "".join(ans)
        
        