class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height)-1
        maxL, maxR = height[0], height[-1] 
        area = 0
        while left < right:
            if maxL <= maxR:
                left += 1
                maxL = max(maxL, height[left])
                water = maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                water = maxR - height[right]

            if water < 0:
                water = 0
            area += water
        return area