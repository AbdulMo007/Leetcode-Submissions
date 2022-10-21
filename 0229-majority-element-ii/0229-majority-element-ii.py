class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        arr = []
        for i in nums:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i]>len(nums)/3:
                arr.append(i)
        return arr
        