class Solution:
    def arrangeCoins(self, n: int) -> int:
        l= 1
        r= n
        if n==1: return 1
        while l<=r:
            m = (l+r)//2
            mid = (m*(m+1))*(1/2)
            if mid <=n:
                l = m+1
            elif mid>n:
                r = m-1
            # else:
            #     return m-1
        return r
        # for i in range(n):
