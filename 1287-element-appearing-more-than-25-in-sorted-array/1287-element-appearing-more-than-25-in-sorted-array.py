class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        s = (len(arr))//4
        
        for i in range (len(arr)-s):
            if arr [i] == arr[i+s]:
                return arr[i]
            
            
            
            
        
#         d = {}
#         #range(start, end, steps)
#         for i in range (len(arr)):
#             if arr[i] in d:
#                 d[arr[i]] += 1
#             else:
#                 d[arr[i]] = 1
                
#         s = (len(arr))/4 
        
#         for i in d:
#             if d[i] > s:
#                 return i
#         # [1,2,3,3]
            
        
        