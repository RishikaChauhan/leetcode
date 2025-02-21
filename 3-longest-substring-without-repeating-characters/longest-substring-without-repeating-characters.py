class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = ""
        mcount = 0
        count = 0
        while i<len(s):
            if s[i] not in res:
                res+=s[i]
                count+=1
                i+=1
                mcount = max(len(res), mcount)
                
            else:
                
                res = res[1:]
                
            # mcount = max(count, mcount)
        return mcount