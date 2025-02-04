class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)
        mm0 = 0
        mm1 = 0

        for i in range(l):
            m0 = '0' if i%2 == 0 else '1'
            m1 = '1' if i%2 == 0 else '1'
            if s[i] != m0:
                mm0+=1
            else:
                mm1+=1
        return min(mm0, mm1)