class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k = 0
        ans = []
        
        for i in range (len(nums)):
            k += nums[i]
            ans.append(k)
        return (ans)