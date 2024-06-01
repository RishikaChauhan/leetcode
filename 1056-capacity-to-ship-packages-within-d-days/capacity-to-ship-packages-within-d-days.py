class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def capa(cap):
            ships, currcap = 1, cap
            for w in weights:
                if currcap<w:
                    ships+=1
                    currcap = cap
                currcap -=w
            return ships<= days

        while l<=r:
            cap = (l+r)//2
            if capa(cap):
                
                res = min(cap, res)
                r = cap-1
            else:
                l = cap+1
        return res

        
        
