class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = len(nums)
        nums = set(nums) 
        j = len(nums)
        
        return k != j
        
#         for i in range (len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return True 
#         return False
        
        