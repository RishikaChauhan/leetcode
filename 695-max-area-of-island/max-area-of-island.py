class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Maintain a set of visited cells
        visited = set()

        def dfs(m, n):
            # Check boundary conditions and whether the cell is already visited or is water
            if (m < 0 or m >= len(grid) or 
                n < 0 or n >= len(grid[0]) or 
                (m, n) in visited or grid[m][n] == 0):
                return 0

            # Mark the cell as visited
            visited.add((m, n))
            
            # Compute the area by DFS on all four possible directions
            area = 1
            area += dfs(m + 1, n)
            area += dfs(m - 1, n)
            area += dfs(m, n + 1)
            area += dfs(m, n - 1)
            return area
        
        max_area = 0
        # Iterate over each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    # Calculate area for the current island
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
