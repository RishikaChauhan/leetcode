class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b':1, 'a':1,'l':2, 'o':2, 'n':1}

        res = []
        for i in d.keys():
            res.append(text.count(i)//d[i])
        return min(res)