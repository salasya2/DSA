class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        res = 0

        queue = deque([])

        n = len(grid)
        m = len(grid[0])
        visited = defaultdict(bool)

        for i in range(n):

            for j in range(m):

                if grid[i][j] == 2:

                    queue.append([i,j,0])
                    visited[(i,j)] = True
        
        res = 0
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            for i in range(len(queue)):
                r,c,level = queue.popleft()

                for dr,dc in DIR:

                    nr , nc  = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != 1 or visited[(nr,nc)] == True:
                        continue
                    
                    queue.append([nr,nc,level + 1])
                    visited[(nr,nc)] = True
                    grid[nr][nc] = -(level + 1)
        

        for i in range(n):

            for j in range(m):

                if grid[i][j] == 1:
                    return -1
                
                res = min(grid[i][j],res)
        return -res
            
        

            
        