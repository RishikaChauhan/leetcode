class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r = 0,k-1
        res, total = 0,0
        window = s[l:k]
        # print(window)
        count = window.count('a')+window.count('e')+window.count('i')+window.count('o')+window.count('u')
        for r in range(k, len(s)):
            window += s[r]
            window = window[1:]
            # print(window)
            if count ==k: return k
            count = max(count, window.count('a')+window.count('e')+window.count('i')+window.count('o')+window.count('u'))
        return count