class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
         - m x n rect islands -> borders are both pacific and Atlantic

         - pacific will touch where i = 0 or j = 0
         - atlantic will touch where i = m-1 or j = n-1

         - water can flow from r,c to nr,nc if height[r][c] >= height[nr][nc]
         - report all the cells from where the water can flow to both atlantic and pacific oceans

         - approach is to take all the cells touching atlantic or pacific and mark each cell in grid as being touched by atlantic or pacific or both

        '''

        m = len(heights)
        n = len(heights[0])

        Dir = [[-1,0],[1,0],[0,-1],[0,1]]

       
        def dfs(r,c,reachable_set):

            reachable_set.add((r,c))

            for dr,dc in Dir:

                nr , nc = dr + r, dc + c

                if nr < 0 or nr >= m or nc < 0 or nc >=n or (nr,nc) in reachable_set or heights[r][c] > heights[nr][nc] :
                    continue
                dfs(nr,nc,reachable_set)
        pacific = set()
        atlantic = set()
        for c in range(n):

            dfs(0,c,pacific)
            dfs(m-1,c,atlantic)
        for r in range(m):
            dfs(r,0,pacific)
            dfs(r,n-1,atlantic)
        
        return list(pacific & atlantic)

       
        return res 
        # O(m*n) #O(m*n)     


                    
                


