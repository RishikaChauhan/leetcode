class Solution:
    def maxArea(self, height: List[int]) -> int:
        mv = 0
        left = 0
        right= len(height)-1
        mv = min(height[left], height[right])*(right-left)
        while left<right:
            if height[left]>height[right]:
                right-=1
                v = min(height[left], height[right])*(right-left)
                mv = max(mv, v)
            
            else:
                left+=1
                v = min(height[left], height[right])*(right-left)
                mv = max(mv, v)
        return mv