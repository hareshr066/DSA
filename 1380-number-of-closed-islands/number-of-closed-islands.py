
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            closed = True
            for dr, dc in directions:
                result = dfs(r + dr, c + dc)
                closed = closed and result
            return closed
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count
