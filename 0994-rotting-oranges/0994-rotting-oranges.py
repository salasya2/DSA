class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        res = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 2:
                    queue.append([i,j,0])
                if grid[i][j] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
        while queue:

            r,c,time = queue.popleft()
            
            print(r,c,time)
            if fresh == 0:
                return res
            
            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr,nc = dr + r, dc + c

                if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != 1:
                    continue
                fresh -= 1
                grid[nr][nc] = 2
                queue.append([nr,nc,time+1])
                res = max(time + 1,res)
        
        return -1