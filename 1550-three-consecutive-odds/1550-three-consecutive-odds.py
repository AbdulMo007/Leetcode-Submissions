class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        s = ""
        for i in arr:
            s += str(i%2)
        return "111" in s
    
        # return "111" in "".join([str(i%2) for i in arr])
        
#         for i in range (len(arr)-2):
#             if arr[i] % 2 == 1:
#                 if arr[i+1]%2 == 1:
#                     if arr [i+2]%2 == 1:
#                         return True
#         return False
         
        