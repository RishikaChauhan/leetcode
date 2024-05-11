class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        r = s[::-1]

        if s==r: return True
        
        for i in range(len(s)):
            if (s[:i] + s[i + 1:] == r[:l - i - 1] + r[l - i:] 
                    or r[:i] + r[i + 1:] == s[:l - i - 1] + s[l - i:]):
                return True
            # k=s[:i]+s[i+1:]
            # print(k)
            # w=t.replace(s[-1*i-1],"")
            # if k==k[::-1]: return True
        return False