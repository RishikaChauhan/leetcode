class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # d = {}
        # if wall == [[1],[1],[1]]: return 3
        # w = sum(wall[0])
        # # for i in range(1, w):
        # for i in wall:
        #     for j in range(len(i)):
        #         d[sum(i[:j])]=1+ d.get(sum(i[:j]),0)
        # d[0]=0
        # d[w]=0
        # return w-(max(list(d.values())))
        countGap = { 0 : 0 }

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())