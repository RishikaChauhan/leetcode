class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ini = (0,0)
        d = {}
        d["N"] = [0,1]
        d["S"] = [0,-1]
        d["E"] = [1,0]
        d["W"] = [-1,0]
        x,y = 0,0
        res = [(0,0)]
        # path = path.split("")
        for i in path:
            x = x+ d[i][0]
            y = y+ d[i][1]
            # print(x,y)
            # print(res)
            if (x,y) in res:
                return True
            else:
                res.append((x,y))
            # if x==0 and y==0:
            #     return True
        return False 