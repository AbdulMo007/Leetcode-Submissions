class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = (len(arr)-1)
        left = 1
        right = n-1
        
        
        while left <= right:
            mid = (left + right)//2 #index 
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            
            if arr[mid-1]<arr[mid]:
                left = mid + 1
            else:
                right = mid -1
# [0,1,2,0]

  