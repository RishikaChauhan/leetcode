class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # sec = set(path[1] for path in paths)
        # fir = set(path[0] for path in paths)
        # ans = sec-fir
        # # return ans.pop()

        dest = {}
        source = {}
        for i in paths:
            dest[i[1]] = 1
            source[i[0]] = 1
        print(dest, source)
        for i in dest:
            if i not in source:
                return i