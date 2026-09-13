class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0
        while i < j:
            curr_area = (j - i) * min(heights[j], heights[i])
            area = max(area, curr_area)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return area