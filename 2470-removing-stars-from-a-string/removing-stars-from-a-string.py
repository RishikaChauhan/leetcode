class Solution:
    def removeStars(self, s: str) -> str:
        st = ''
        for i in s:
            if i!='*':
                st+=i
            else:
                st= st[:-1]
        return st
        
        
        
        
        
        
        
        
        
        while '*' in s:
            i = s.index('*')
            if i==0:
                continue
            else:
                s= s.replace(s[i-1]+'*', '')
        return s