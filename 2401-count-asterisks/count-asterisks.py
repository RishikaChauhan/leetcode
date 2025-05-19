class Solution:
    def countAsterisks(self, s: str) -> int:
        sl = s.split("|")
        c= 0
        for i in range(0,len(sl),2):
            c+=sl[i].count("*")
        return c