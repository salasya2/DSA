class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])


        res = 0

        queue = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    grid[i][j] = 10000000
                    queue.append([i,j,0])
                if grid[i][j] == 1:
                    fresh+=1
        

        while queue:
            if fresh == 0:
                return res
            for i in range(len(queue)):
                r,c,dist = queue.popleft()
                
                for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr , nc = dr + r, dc + c

                    if nr < 0 or  nc < 0 or nr >= n or nc >= m or grid[nr][nc] != 1:
                        continue
                    queue.append([nr,nc,dist+1])
                    grid[nr][nc] = 2
                    fresh -=1
                
                    res= max(res,dist+1)
        if fresh == 0:
            return res
        return -1