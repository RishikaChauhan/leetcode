class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isalnum():
                print(i)
                t+=i.lower()
                # s.replace(i, "")
        print(s,t)
        return t == t[::-1]
                