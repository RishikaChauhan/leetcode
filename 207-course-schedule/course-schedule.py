class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)<=1: return True
        crsset = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsset[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if crsset[crs]==[]:
                
                return True
            visitSet.add(crs)
            for i in crsset[crs]:
                if not dfs(i): return False
            visitSet.remove(crs)
            crsset[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

