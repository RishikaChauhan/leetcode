class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        w3 = ""
        for i in range(min(l1,l2)):
                w3+=word1[i]+word2[i]
        return w3+ word2[l1:]+word1[l2:]
        # elif l2<l1:
        #     for i in range(l2):
        #         w3+=word1[i]+word2[i]
        #     return w3+ word1[l2:]
        # else:
        #     for i in range(l2):
        #         w3+=word1[i]+word2[i]
        #     return w3

