class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l,r = 0, len(height)-1
        lm,rm = height[l], height[r]
        v = 0

        while l<r:
            # mn = min(height[l], height[r])
            # for i in range(l, r):
            #     if height[i]<mn:
            #         v+=1
            if height[l]<height[r]:
                l+=1
                lm = max(lm, height[l])
                v+=max(0, lm-height[l])

            else:
                r-=1
                rm = max(rm, height[r])
                v+= max(0, rm-height[r])
            
        return v