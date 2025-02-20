class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        v= 0
        while l<r:
            vn=(r-l)*min(height[r], height[l])
            v = max(v,vn)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            # else:
            #     l+=1
            #     r-=1
            
        return v