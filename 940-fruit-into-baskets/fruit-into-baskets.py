import collections
class Solution:
    def totalFruit(self, s: List[int], k=0) -> int:
        count = collections.defaultdict(int)

        l,total = 0, 0
        res = 0
        for r in range(len(s)):
            count[s[r]] +=1
            total+=1
            while len(count)>2:
                f = s[l]
                count[f]-=1
                total-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res