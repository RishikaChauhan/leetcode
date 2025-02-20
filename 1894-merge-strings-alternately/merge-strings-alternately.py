class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        s = ""
        for i in range(m):
            s +=word1[i]+word2[i]
        s = s+ word1[i+1:] if word1[i+1:] else s+word2[i+1:]

        return s