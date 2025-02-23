class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        l1 = len(matrix)
        l2 = len(matrix[0])
        h = l1*l2-1
        while l<=h:
            m = (l+h)//2
            r , c =m//l2, m%l2
            if matrix[r][c]<target:
                l = m+1
            elif  matrix[r][c]>target:
                h = m-1
            else: return True
        return False