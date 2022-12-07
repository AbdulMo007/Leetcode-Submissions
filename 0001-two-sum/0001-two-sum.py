class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        
        for i in range (len(nums)):
            r = target - nums[i]
            if r in D:
                return D[r], i                                          
            D[nums[i]] = i