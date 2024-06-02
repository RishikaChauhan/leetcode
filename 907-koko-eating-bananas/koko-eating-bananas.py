class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r:
            m = (l+r)//2
            total= 0
            for p in piles:
                total+=math.ceil(float(p)/m)
            if total<=h:
                res = m
                r = m-1
            else:
                l= m+1
        return res
        # if h == len(piles): return max(piles)
        # piles.sort()
        # r = sum(piles)
        # l= max(piles)
        # def cap(m):
        #     c, hr = m, 1
        #     if c >hr:
        #         hr+=1
        #         c = m
        #     return hr>h 
             

        # while l<=r:
        #     m = (l+r)//2
        #     if cap(m)>h:
        #         r = m-1
        #     elif cap(m)<h:
        #         l = m+1
        #     else:
        #         return m
        # return l