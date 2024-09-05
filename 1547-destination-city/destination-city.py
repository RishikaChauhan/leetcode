class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # sec = set(path[1] for path in paths)
        # fir = set(path[0] for path in paths)
        # ans = sec-fir
        # # return ans.pop()
        s,d = [],[]

        for i in paths:
            s.append(i[0])
            # d.append(i[1])
        # print(s, d)
        for i in paths:
            if i[1] not in s:
                return i[1]










        # dest = {}
        # source = {}
        # for i in paths:
        #     dest[i[1]] = 1
        #     source[i[0]] = 1
        # # print(dest, source)
        # for i in dest:
        #     if i not in source:
        #         return i