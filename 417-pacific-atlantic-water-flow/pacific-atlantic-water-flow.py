class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row = len(heights)
        cols = len(heights[0])
        pacific,atlantic = set(),set()
        def dfs(r,c,visited,preheight):
            if (r,c) in visited or r<0 or r==row or c<0 or c==cols or heights[r][c]< preheight:
                return 
            visited.add((r,c)) 
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(row-1,c,atlantic,heights[row-1][c])
        for r in range(row):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        res = []
        for r in range(row):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic :
                    res.append([r,c])
        return res 
        