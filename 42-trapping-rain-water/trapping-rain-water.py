from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if the list is empty or has less than 3 bars, no water can be trapped
        if not height or len(height) < 3:
            return 0

        count = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                count += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                count += right_max - height[right]

        return count
