class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        if numRows==2: return [[1], [1,1]]
        else:
            # for i in range(2, numRows):
            res = self.generate(numRows-1)
            ele = res[-1]
            l=[1]
            for j in range(1,len(ele)):
                l.append(ele[j]+ele[j-1])
            l.append(1)
            res.append(l)
            return res