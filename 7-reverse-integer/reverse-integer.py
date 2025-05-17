class Solution:
    def reverse(self, n: int) -> int:
        neg = False
        if n<0:
            neg = True
            n = n*-1

        def r(n, rev):
            if rev >2**31: return 0
            if n == 0:
                return rev
            rem = n%10
            rev = (rev)*10 + rem
            return r(n//10, rev)

        return r(n, 0) if neg == False else r(n, 0)*-1