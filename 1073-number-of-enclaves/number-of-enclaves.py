class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        row = len(grid)
        cols=len(grid[0])
        visited=set()
        
        def dfs(r,c):
            if r<0 or r>= row or c<0 or c>=cols or (r,c) in visited or grid[r][c]==0:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(row):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(row-1,c)
        c=0
        for i in range(row):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    c+=1
        return c 
                    