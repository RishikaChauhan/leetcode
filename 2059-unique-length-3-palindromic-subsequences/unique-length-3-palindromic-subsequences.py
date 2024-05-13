class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans =0
        for i in range(26):
            c = chr(i+ord('a'))
            if c in s:
                first = s.index(c)
                last = s.rindex(c)
                if first != last:
                    u = set()
                    for index in range(first+1, last):
                        u.add(s[index])
                    ans+=len(u)
        return ans
        
        
        
        
        
        l=0
        
        res = set()
        done=[]
        for l in range(len(s)-2):
            r = len(s)-1
            while l<r-1:
                if s[l]==s[r] and s[l] not in done:
                    done.append(s[l])
                    for i in range(l+1,r):
                        res.add(s[l]+s[i]+s[r])
                    r=r-1
                r=r-1
        # print(res)
        return len(set(res))