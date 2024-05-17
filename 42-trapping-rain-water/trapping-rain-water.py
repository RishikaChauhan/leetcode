class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        rheight= height[::-1]
        # k = sorted(list(set(height)), reverse = True)
        
        l =0
        r = len(height)-1
        lh = height[l]
        rh = height[r]
        while l<r:
            if lh<rh:
                l+=1
                lh = max(lh, height[l])
                count +=lh-height[l]
            else:
                r -= 1
                rh = max(rh, height[r])
                count += rh - height[r]
            
        return count
            