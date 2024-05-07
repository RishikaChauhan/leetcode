class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        d = {}
        print(set(pattern))
        if len(pattern)!= len(s): return False
        if len(set(pattern))!= len(set(s)): return False
        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                d[pattern[i]]= [i,s[i]]
        res1 = []
        for i in pattern:
            res1.append(d[i][1])
        return res1==s
        # print(d)
        # return True
        