class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        res = 0 
        Dir = [[1,0],[-1,0],[0,-1],[0,1]]

        def dfs(r,c):

            grid[r][c] = "0"

            for dr,dc in Dir:
                
                nr,nc = r + dr , c + dc

                if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != "1":
                    continue
                
                dfs(nr,nc)
            
        
        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        
        return res

        # O(m*n) O(m*n)