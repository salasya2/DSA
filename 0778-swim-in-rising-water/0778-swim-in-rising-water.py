class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
            0,0 , 1
            0,1,2
        
        '''
        res = 0
        n = len(grid)

        if n == 1:
            return grid[0][0]
        min_heap = [(grid[0][0],0,0)]
        
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]

        Dir = [[0,1],[0,-1],[1,0],[-1,0]]

        while min_heap:
            elevation,i,j= heapq.heappop(min_heap)
            if i == n-1 and j==n-1:
                return dp[n-1][n-1]
            
            for dr,dc in Dir:
                nr,nc = dr + i, dc + j

                if nr < 0 or nc < 0 or nr >= n or  nc >= n:
                    continue
                
                if max(elevation,grid[nr][nc]) < dp[nr][nc]:
                    dp[nr][nc] = max(elevation,grid[nr][nc]) 
                    heapq.heappush(min_heap,(dp[nr][nc],nr,nc))
         
        return dp[n-1][n-1]
            

