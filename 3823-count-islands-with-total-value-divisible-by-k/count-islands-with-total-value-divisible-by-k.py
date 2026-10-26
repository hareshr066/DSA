
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        def dfs(r, c):
            vis[r][c] = True
            total = grid[r][c]
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n
                    and not vis[nr][nc]
                    and grid[nr][nc] > 0):
                    total += dfs(nr, nc)
            return total
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not vis[i][j]:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        ans += 1
        return ans
