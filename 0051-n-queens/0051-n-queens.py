class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        res = []
        col = 0
        pos = 0
        neg = 0
        


        def dfs(i):
            nonlocal col,pos,neg
            

            if i==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for j in range(n):
                
                if ((col & (1 << j)) or (pos & ( 1<< (i+j))) or (neg & ( 1 << (i - j + n)))):
                    continue
                
                col ^= (1 << j)
                pos ^= (1 << (i + j))
                neg ^= (1 << (i - j + n))
                board[i][j] = 'Q'

                dfs(i+1)
                
                col ^= (1 << j)
                pos ^= (1 << (i + j))
                neg ^= (1 << (i - j + n))
                board[i][j] = '.'
            
        dfs(0)
        return res

                    

        