class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        b = max(nums)
        nums.remove(b)
        c = max(nums)
        return ((b-1)*(c-1))
    
        
        
        
        
# function vs methods
        
        
#         nums.sort()
        
#         return (nums[-1]-1)*(nums[-2]-1)