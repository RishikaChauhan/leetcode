class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l=r=0
        lent = 0
        for i in range(len(s)):
            char = s[i]
            if char in seen and seen[char]>=l:
                l = seen[char]+1
            else:
                lent = max(lent, i-l+1)
            seen[char]= i
        return lent