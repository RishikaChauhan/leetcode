import string

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # f = 0
        mxl = -1
        if s[0]==s[-1]:
            return len(s)-2
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if s[i]==s[j]:
                    length = j-1-i
                    mxl = max(mxl, length)
                    break
        return mxl
        #         lc = f-j
        #         c = min(c, lc)
        # return len(s)-c