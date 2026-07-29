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

        queue = deque()

        for i in range(0,m):
            queue.append([i,0])
        
        for j in range(0,n):
            queue.append([0,j])
        
        visited = {}

        while queue:

            r,c = queue.popleft()
            if (r,c) in visited:
                continue
            visited[(r,c)] = 1

            for dr,dc in Dir:

                nr,nc = r + dr , c + dc

                if nr < 0 or nc < 0 or  nr >= m or nc >=n or heights[r][c] > heights[nr][nc] or (nr,nc) in visited:
                    continue
                queue.append([nr,nc])
        
        for i in range(0,m):
            queue.append([i,n-1])
        for i in range(0,n):
            queue.append([m-1,i])
        # print(visited)
        # print("-----------")
        res = []
        while queue:

            r,c = queue.popleft()
            
            if (r,c) in visited and visited[(r,c)] == 1:
                visited[(r,c)] = 0
                res.append([r,c])
            else:
                visited[(r,c)] = 2
            
            for dr,dc in Dir:

                nr , nc = r + dr , c + dc

                if nr < 0 or nr >= m or nc <0 or  nc >= n or heights[r][c] > heights[nr][nc] or ((nr,nc) in visited and visited[(nr,nc)]!=1):
                    continue
                queue.append([nr,nc])
        print(visited)
        return res 
                


                    
                


