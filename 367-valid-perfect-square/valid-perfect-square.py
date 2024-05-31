class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l<=r:
            m = (l+r)//2
            s = m*m
            if s>num:
                r = m-1
            elif s<num:
                l = m+1
            else: 
                return True
        return False