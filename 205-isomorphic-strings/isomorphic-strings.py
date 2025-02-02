class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def fun(s):
            d = {}
            for i in s:
                if i not in d.keys():
                    d[i] = len(d)+1
            # print(d, d.values())
            return d

        d1 = fun(s)
        d2 = fun(t)
        q = []
        for i in s:
            q.append(d1[i])
        r = []
        for i in t: 
            r.append(d2[i])
        print(q,r)
        return q==r