class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = True
        dsc = True 
        
        for i in range (len(nums)-1):
            if nums[i]>nums[i+1]:
                asc = False
            if nums[i]<nums[i+1]:
                dsc = False
        return asc or dsc 
        