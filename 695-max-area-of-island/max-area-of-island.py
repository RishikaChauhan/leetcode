# m,n
# m+1, n+1
# m+1, n-1
# m-1, n+1
# m-1, n-1


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        s = set()
        def dfs(m,n):
            if (m,n) in s or grid[m][n]==0 or (m < 0 or m >= len(grid) or 
                n < 0 or n >= len(grid[0])):
                return 0
            
            
            if grid[m][n]==1:
                area=1
                s.add((m,n))
                if m+1<len(grid): area+=dfs(m+1,n)
                if m-1>=0: area+=dfs(m-1,n)
                if n-1>=0: area+=dfs(m,n-1)
                if n+1<len(grid[0]): area+=dfs(m,n+1)
            
            return area


        m1= len(grid)
        n1=len(grid[0])
        max_area = 0
        for i in range(m1):
            for j in range(n1):
                if grid[i][j] ==1 and (i,j) not in s:
                    
                    area = dfs(i,j)
                    max_area = max(max_area, area)
        return max_area
