class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        
        while left < right:
            if height[left] > height[right]:
                temp = height[right] * (right - left)
                area = max(area,temp)
                right -= 1
            else :
                temp = height[left] * (right - left)
                area = max(area,temp)
                left += 1
        return area
