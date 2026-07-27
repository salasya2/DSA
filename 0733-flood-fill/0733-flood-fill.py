class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        '''
        - n * m grid
        - change sr,sc to color 
        - change all the adjacent nodes having same val of sr,sc to color.
        - store the val into a var to keep modifying. 
        
        '''
        Dir = [[-1,0],[0,1],[1,0],[0,-1]]
        val = image[sr][sc]
        if val == color:
            return image
        def dfs(r,c,val):
            nonlocal color
            image[r][c] = color

            for dr,dc in Dir:

                nr,nc = r + dr,c + dc

                if nr < 0 or nc < 0 or nr >=n or nc >=m or image[nr][nc] != val:
                    continue
                
                dfs(nr,nc,val)
            
        dfs(sr,sc,val)
        return image


            

        