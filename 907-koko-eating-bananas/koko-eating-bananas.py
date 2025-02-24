class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            m = (l+r)//2
            if sum(ceil(i/m) for i in piles)<=h:
                r = m
            else:
                l = m+1
        return l
        
        
        
        
        
        
        
        # # piles.sort()
        # l = 1
        # r = max(piles)
        # def fun(cnt):
        #     return sum(ceil(i/cnt) for i in piles)<=h

        # while l<r:
        #     m = (l+r)//2
        #     if fun(m):
        #         r = m
        #     else: l =m+1

        # return l