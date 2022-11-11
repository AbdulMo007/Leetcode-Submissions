class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #2 pointers 1 from r and 1 from l
        # #minus left pointer index from right index = W
        # #area = w * min (H[l]),H[R])
        # if area > max area
        #  then max area = area 
        #     return max area
        
        l = 0
        r = (len(height)-1)
        max_area = 0
        while l < r:
            W = r - l
            H = min(height[l],height[r])
            area = W * H
            if area > max_area:
                max_area = area            
            if height[l]< height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        
            
            
        