class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        mapChar={}
        mapWord={}
        print(set(pattern))
        if len(pattern)!= len(s): return False
        if len(set(pattern))!= len(set(s)): return False
        for char,word in zip(pattern,s):
            if char not in mapChar:
                if word in mapWord:
                    return False
                else:
                    mapChar[char]=word
                    mapWord[word]=char
            else:
                if mapChar[char]!=word:
                    return False
        return True

        
