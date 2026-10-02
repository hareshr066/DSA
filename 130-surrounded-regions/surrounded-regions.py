class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        cols= len(board[0])
        visited=set()
        def dfs(r,c,o):
            if r<0 or r>=row or c<0 or c>=cols or (r,c) in visited or board[r][c]=="X":
                return False
            touches=(r == 0 or r == row-1 or c == 0 or c == cols-1)
            visited.add((r,c))
            o.append((r,c))
            touchingbound = dfs(r+1,c,o) or touches
            touchingbound = dfs(r-1,c,o) or touchingbound
            touchingbound = dfs(r,c+1,o) or touchingbound
            touchingbound = dfs(r,c-1,o) or touchingbound
            return touchingbound
        touchingbound=False
        for r in range(row):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visited:
                    o=[]
                    touchingbound=dfs(r,c,o) 
                    if not touchingbound :
                        for x,y in o:
                            board[x][y]="X"

            
        
        