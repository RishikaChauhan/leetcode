class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        ms1 = sorted(s1)
        for i in range(len(s2)-l1+1):
            ms2 = s2[i:i+l1]
            if sorted(ms2)==ms1:
                return True
        return False