class Solution:
    def findDuplicate(self, head: List[int]) -> int:
        res = set()

        for i in head:
            l = len(res)
            res.add(i)
            if len(res)==l:
                return i
            
        