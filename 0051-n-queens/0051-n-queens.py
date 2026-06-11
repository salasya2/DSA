class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        s = ["." for _ in range(n)]
        board = ["".join(s)] * n
        res = []
        visited = []
        


        def dfs(i):
            
            

            if i>=n:
                res.append(board.copy())
                return
            
            for j in range(n):
                
                flag = False
                for pair in visited:
                    
                    if i == pair[0] or j == pair[1] or i - j == pair[0] - pair[1] or i + j == pair[0] + pair[1]:
                        flag = True
                        break
                if flag == False:

                    s[j] = 'Q'
                    board[i] = "".join(s) 
                    s[j]='.'
                    visited.append((i,j))
                    dfs(i+1)
                    visited.pop()
                    board[i] = "".join(s)
                    
        dfs(0)
        return res

                    

        