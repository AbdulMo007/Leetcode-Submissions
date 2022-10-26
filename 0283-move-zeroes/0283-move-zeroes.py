class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        j = 0
        k = 0
        
        while k < (len(nums)):
            if nums[k] != 0:
                if nums[j] == 0:
                    nums[k], nums [j] = nums[j], nums[k]
                j += 1
            k += 1
                
                    
        
        
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # i = 5
#         for i in range (len(nums)):
#             if nums [i] == 0:
#                 nums.append(nums[i])
#                 nums.remove(nums[i])
               
            
        