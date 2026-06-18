class Solution:
    def solve(self, board: List[List[str]]) -> None:

        n = len(board)
        m = len(board[0])

        q = deque([])

        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = '#'
                q.append([i,0])
            if board[i][m-1] == 'O':
                board[i][m-1] = '#'
                q.append([i,m-1])

        for j in range(1,m):

            if board[0][j] == 'O':
                board[0][j] = '#'
                q.append([0,j])
            
            if board[n-1][j] == 'O':
                board[n-1][j] = '#'
                q.append([n-1,j])
        
        DIR = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:

            r,c = q.popleft()

            for dr, dc in DIR:

                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr >= n or nc >= m or board[nr][nc] == '#' or board[nr][nc] == 'X':
                    continue
                
                q.append([nr,nc])
                board[nr][nc] = '#'
        
        for i in range(n):
            for j in range(m):
                
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
    