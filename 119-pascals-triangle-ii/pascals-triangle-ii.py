class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [0,0 ]
        if rowIndex ==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        else:
            x = [1]
            k = self.getRow(rowIndex-1)
            for i in range(len(k)-1):
                x.append(k[i]+k[i+1])
            x.append(1)
            return x
        # t[0]=[1]
        # t[1] = [1,1]
