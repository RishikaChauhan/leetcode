class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1: return "1"
        n = self.countAndSay(n-1)
        res = ''
        i = 0
        while i < len(n):
            j = i
            while j<len(n) and n[j]==n[i]:
                    j+=1
            res = res+str(j-i) + n[i]
            i = j
        return res
                
