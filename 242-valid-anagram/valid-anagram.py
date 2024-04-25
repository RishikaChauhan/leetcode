class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        if set(t)!=set(s): return False
        # if sorted(t)==sorted(s):
        #     return True
        # return False
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0)+1
        for char in t:
            if char not in counter or counter[char]==0:
                return False
            else:
                counter[char]-=1
        return True