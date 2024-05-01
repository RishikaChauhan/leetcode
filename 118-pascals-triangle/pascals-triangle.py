class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        res =[[1], [1,1]]
        for i in range(2, numRows):
            ele = res[i-1]
            l=[1]
            for j in range(1,len(ele)):
                l.append(ele[j]+ele[j-1])
            l.append(1)
            res.append(l)
        return res