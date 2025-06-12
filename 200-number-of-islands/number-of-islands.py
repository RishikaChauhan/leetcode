class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        visit=set()
        island = 0
        def dfs(row, col):
            if (row,col) not in visit:
                if row==-1 or row==len(grid): return
                if col ==-1 or col ==len(grid[0]): return
        
                if grid[row][col] =="1":
                    
                    visit.add((row, col))
                    dfs(row+1, col)
                    dfs(row-1, col)
                    dfs(row, col-1)
                    dfs(row, col+1)
        for row in range(len(grid)):
                    
            for col in range(len(grid[0])):
                if (row, col) not in visit and grid[row][col]=="1":
                    dfs(row, col)
                    island+=1
        return island
