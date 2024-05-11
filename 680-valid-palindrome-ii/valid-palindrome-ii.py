class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        r = s[::-1]

        if s==r: return True
        
        for i in range(l):
            
            if s[i] == r[i]:
                continue
            if (s[:i] + s[i + 1:] == r[:l - i - 1] + r[l - i:] 
                    or r[:i] + r[i + 1:] == s[:l - i - 1] + s[l - i:]):
                return True
            return False

        l = len(s)
        r = s[::-1]
        if s == r:
            return True

        for i in range(l):
            if s[i] == r[i]:
                continue
            if (s[:i] + s[i + 1:] == r[:l - i - 1] + r[l - i:] 
                    or r[:i] + r[i + 1:] == s[:l - i - 1] + s[l - i:]):
                return True
            
            return False