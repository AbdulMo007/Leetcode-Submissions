class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        D = {}
        sum = 0
        for i in range (len(nums)):
            if nums[i] not in D:
                D[nums[i]] = 1
            else:
                D[nums[i]] += 1
        for i in D:
            if D[i] == 1:
                sum += i
        return sum
        
        
        