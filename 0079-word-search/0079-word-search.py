class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        if len(word) == 0:
            return False
        built = []
        def find(i,r,c):

            if i > len(word):
                return False 
            if i == len(word):
                return True
            
           
            val = board[r][c]
            board[r][c] = "#"
            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:

                nr,nc = dr+r,dc+c

                if nr < 0 or nc <0 or nr >= n or nc >=m or board[nr][nc] != word[i] or board[nr][nc] == "#":
                    continue
                
                if find(i+1,nr,nc):
                    return True
            
            board[r][c] = val
            return False
        
        for i in range(n):
            for j in range(m):

                if board[i][j] == word[0]:
                    if find(1,i,j):
                        return True
        return False
