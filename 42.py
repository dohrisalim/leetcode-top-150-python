class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        trapped_water = 0

        while left < right:
            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])
            if max_left < max_right:
                trapped_water += max_left - height[left]
                left += 1
            else:
                trapped_water += max_right - height[right]
                right -= 1

        return trapped_water
        