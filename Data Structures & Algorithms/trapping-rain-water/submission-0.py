class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0
        while l <= r:
            if maxL <= maxR:
                currentWater = maxL - height[l]
                if currentWater > 0:
                    water += currentWater
                
                maxL = max(height[l], maxL)
                l += 1
            else:
                currentWater = maxR - height[r]
                if currentWater > 0:
                    water += currentWater
                
                maxR = max(height[r], maxR)
                r -= 1
        
        return water
