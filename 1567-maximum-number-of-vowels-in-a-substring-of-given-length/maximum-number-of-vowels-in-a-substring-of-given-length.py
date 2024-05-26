class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r = 0,k-1
        res, total = 0,0
        window = s[l:k]
        print(window)
        count = window.count('a')+window.count('e')+window.count('i')+window.count('o')+window.count('u')
        # print(count)
        res = count
        for r in range(k, len(s)):
            nc = count
            if s[r] in ['a', 'e','i', 'o', 'u']:
                nc+=1
            window += s[r]
            if window[0] in ['a', 'e','i', 'o', 'u']:
                nc-=1
            window = window[1:]
            # print(nc, window)
            if nc ==k: return k
            res = max(res,nc)
            # print(res)
            count = nc
        return res