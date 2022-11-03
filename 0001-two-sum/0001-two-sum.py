class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        
        for ind, val in enumerate(nums):
            R = target - val
            if R in D:
                return D[R], ind
            D [val] = ind              
            