class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range (len(arr)-1):
        #     if arr[i+1]<arr[i]:
        #         return i
            # arr = [0,1,2,0]
        n = len(arr)
        left = 1
        right = n - 2
        while left <= right: 
            #left = 2, right = 2
            mid = (left + right) // 2 #mid = 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid #returns 2
            if arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        