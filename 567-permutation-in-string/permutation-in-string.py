class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)-len(s1)+1):
            ss = s2[i: i+len(s1)]
            if sorted(ss) == s1:
                return True
        return False