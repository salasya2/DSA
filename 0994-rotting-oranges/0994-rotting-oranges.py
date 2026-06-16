class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        res = 0

        queue = deque([])

        n = len(grid)
        m = len(grid[0])
        fresh = 0

        for i in range(n):

            for j in range(m):

                if grid[i][j] == 2:

                    queue.append([i,j,0])
                    grid[i][j] = 10000000
                
                if grid[i][j] == 1:
                    fresh+=1
        
        res = 0
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            if fresh == 0:
                break
            for i in range(len(queue)):
                r,c,level = queue.popleft()

                for dr,dc in DIR:

                    nr , nc  = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != 1 :
                        continue
                    
                    queue.append([nr,nc,level + 1])
                    
                    grid[nr][nc] = -(level + 1)
                    res = max(res, level+1)
                    fresh -= 1
        
        if fresh == 0:
            return res
        
        return -1
            
        

            
        