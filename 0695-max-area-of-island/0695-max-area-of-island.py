class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        Dir = [[-1,0],[1,0],[0,1],[0,-1]]

        n = len(grid)
        m = len(grid[0])


        def dfs(r,c,area):

            area += 1

            grid[r][c] = 0

            for dr,dc in Dir:

                nr,nc = dr + r,dc + c

                if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == 0:
                    continue

                area = max(area,dfs(nr,nc,area))
            
            return area
        area = 0
        for i in range(n):

            for j in range(m):

                if grid[i][j] == 1:
                    area = max(area,dfs(i,j,0))
        return area
        