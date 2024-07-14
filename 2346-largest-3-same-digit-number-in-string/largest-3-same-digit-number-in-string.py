class Solution:
    def largestGoodInteger(self, num: str) -> str:
        g = "" or 0
        for i in range(len(num)-2):
            if num[i]==num[i+1]== num[i+2]:
                t = num[i:i+3]
                if int(t)>=int(g):
                    g = t
        if g ==0:
            return ""
        return g
        return ""