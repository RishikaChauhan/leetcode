class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # mp = 0
        m,n = len(grid), len(grid[0])
        seen = set()
        
        
        def dfs(r,c):
            
            if r<0 or r>m-1 or c<0 or c>n-1 or grid[r][c]==0:
                return 1     
            if (r,c) in seen:
                return 0     
            seen.add((r,c))
            p= dfs(r+1, c)+dfs(r-1,c)+dfs(r,c+1) +dfs(r,c-1)
            
            return p




        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)
                    
        return 0