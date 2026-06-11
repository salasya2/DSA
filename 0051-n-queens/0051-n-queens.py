class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        res = []
        col = [False] * n
        posdiag = [False] * (n*2)
        negdiag = [False] * (n*2)
        


        def dfs(i):
            
            

            if i==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for j in range(n):
                
                if col[j] or posdiag[i + j] or negdiag[i-j+n]:
                    continue
                
                col[j] = True
                posdiag[i+j] = True
                negdiag[i-j + n] = True
                board[i][j] = 'Q'
                dfs(i+1)
                col[j] = False
                posdiag[i+j] = False
                negdiag[i-j + n] = False
                board[i][j] = '.'
            
        dfs(0)
        return res

                    

        