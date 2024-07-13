class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        # print(d["a"])
        for i in strs:
            a = "".join(sorted(i))
            # print(a)
            # print(d)
            if a in list(d.keys()):
                d[a].append(i)
                # print(d[a])
            else:
                d[a]=[i]
                # pass
        return list(d.values())