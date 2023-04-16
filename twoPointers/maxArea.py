class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height)-1
        while  l < r:
            area = (r - l) * min(height[r], height[l])
            if area > maxArea:
                maxArea = area
            if height[l] <= height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return maxArea
 
