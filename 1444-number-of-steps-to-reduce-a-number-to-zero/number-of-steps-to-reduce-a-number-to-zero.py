class Solution:
    def numberOfSteps(self, num: int) -> int:

        def helper(n, c):
            if n==0: return c
            if n%2 == 0: 
                n= n//2
                c+=1
            else:
                n = n-1
                c+=1
            return helper(n,c)
        return helper(num, 0)
