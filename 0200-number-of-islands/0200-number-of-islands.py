class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        visited = []
        stack = []
        res = 0
        idx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):

            nonlocal n, m

            if i >= n or j >= m or i < 0 or j < 0 or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for dr, dc in idx:
                dfs(i + dr, j + dc)

        for i in range(n):

            for j in range(m):

                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
