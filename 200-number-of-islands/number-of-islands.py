class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        island = 0
        visit = set()
        def dfs(m,n):
            if (m,n) not in visit:
                # if row==-1 or row==len(grid): return
                # if col ==-1 or col ==len(grid[0]): return
                if -1<m<len(grid) and -1<n<len(grid[0]):
                    if grid[m][n]=="1":
                        visit.add((m,n))
                        dfs(m-1, n)
                        dfs(m+1, n)
                        dfs(m,n-1)
                        dfs(m,n+1)
                        # island+=1
                
            else: return
        #     if (row,col) not in visit:
        #         if row==-1 or row==len(grid): return
        #         if col ==-1 or col ==len(grid[0]): return
        
        #         if grid[row][col] =="1":
                    
        #             visit.add((row, col))
        #             dfs(row+1, col)
        #             dfs(row-1, col)
        #             dfs(row, col-1)
        #             dfs(row, col+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visit and grid[i][j] == "1":
                    dfs(i,j)
                    island+=1
                    
        return island
        
        # if not grid: return 0
        # visit=set()
        # island = 0
        # def dfs(row, col):
        #     if (row,col) not in visit:
        #         if row==-1 or row==len(grid): return
        #         if col ==-1 or col ==len(grid[0]): return
        
        #         if grid[row][col] =="1":
                    
        #             visit.add((row, col))
        #             dfs(row+1, col)
        #             dfs(row-1, col)
        #             dfs(row, col-1)
        #             dfs(row, col+1)
        # for row in range(len(grid)):
                    
        #     for col in range(len(grid[0])):
        #         if (row, col) not in visit and grid[row][col]=="1":
        #             dfs(row, col)
        #             island+=1
        # return island
