class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = t
        # s = s[::-1]
        