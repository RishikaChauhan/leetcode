class Solution:
    def isPalindrome(self, s: str) -> bool:
        # j = 
        # s = "".join(s)
        s = "".join(c for c in s if c.isalnum()).lower()
        print(s)
        return s == s[::-1]