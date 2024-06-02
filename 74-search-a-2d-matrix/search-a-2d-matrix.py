class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = n*m-1
        while start<=end:
            mid = (start+end)//2
            i = mid//m
            j = mid%m
            if target== matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                end = mid-1
            else: start = mid+1
        return False












        # if target<matrix[0][0]:return False
        # if target>matrix[-1][-1]: return False
        
        # f = [i[0] for i in matrix]
        # target_in = 0
        
        # if len(matrix)>1:
        #     for i in range(len(f)):
        #         if f[i]==target:
        #             return True
        #         elif f[i]>target:
        #             target_in = i-1
        #             break
        # if matrix[-1][0]<target: target_in = -1
                
        # ls = matrix[target_in]
        # print(ls)
        # l = 0
        # r = len(ls)-1
        # while l<=r:
        #     m= (l+r)//2
        #     print(m)
        #     if ls[m]> target:
        #         r = m-1
        #     elif ls[m]<target:
        #         l = m+1
        #     elif ls[m]==target:
        #         return True
        # return False
        