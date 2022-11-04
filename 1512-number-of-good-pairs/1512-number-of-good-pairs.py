class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        new_d={}
        # 1,2,3,1,1,3
        count = 0
        for i in nums:
            if i not in new_d:
                new_d[i]=1
            else:
                count+=new_d[i]
                new_d[i]+=1
        return count
        
        
        
        
        
        
        
#         ans = 0
#         for i in range (len(nums)):
#             for j in range (len(nums)):
#                 if i<j and nums[i] == nums[j]:
#                     ans += 1
#         return ans
        