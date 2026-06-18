class DSU:
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = list(range(n+1))
    
    def find(self, node):

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, u,v):

        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

        return True
    
    def connected(self,u,v):
        if self.find(u) == self.find(v):
            return True
        return False
    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        n = len(board)
        m = len(board[0])

        dsu = DSU(n*m + 1)

        DIR = [[0,1],[0,-1],[1,0],[-1,0]]

        def index(i,j):
            return i*m + j
        for i in range(n):

            for j in range(m):

                if board[i][j] == 'O':

                    if i == 0 or j == 0 or i == n-1 or j == m-1:
                        dsu.union(n*m, index(i,j))
                    
                    else:
                        for dr, dc in DIR:

                            nr = dr + i
                            nc = dc + j

                            if nr < 0 or nc < 0 or nr >=n or nc >=m or board[nr][nc] != 'O':
                            
                                continue
                            
                            dsu.union(index(nr,nc),index(i,j))
                    # print(dsu.parent)

        
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'O':
                    
                    continue
                if not dsu.connected(index(i,j),n*m):
                    board[i][j] = 'X'
                
                            
