class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return n>0 and 3**19 %n==0
        # def div(n):
        if n<=0: return False
        while n%3 ==0:
            n = n//3
        return n==1  