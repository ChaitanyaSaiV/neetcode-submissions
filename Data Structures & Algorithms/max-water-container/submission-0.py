class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")
        left = 0
        right = len(heights) - 1

        while left < right:
            current_area = (min(heights[left],heights[right])) * (right - left)
            area = max(area, current_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return area