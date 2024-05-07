class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        d = {}
        print(set(pattern))
        if len(pattern)!= len(s): return False
        if len(set(pattern))!= len(set(s)): return False
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]]= pattern[i]
        res1 = ''
        for i in s:
            res1+=d[i]
        return res1==pattern
