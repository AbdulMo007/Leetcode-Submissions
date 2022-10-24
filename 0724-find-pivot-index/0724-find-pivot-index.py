class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # pi = sum(left i's)==sum(right i's)
        # if i==0 then ls = 0, if i==-1 then rs = 0
        # find pi
        
        leftsum = 0

        total = sum(nums)
        for i in range (len(nums)):
            rightsum = total - nums[i] - leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
        