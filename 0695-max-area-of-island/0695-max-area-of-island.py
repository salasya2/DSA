class DSU:

    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [1] *(n+1)
    def find(self,node):

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
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
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def index(i,j):
            return i * m + j
        
        res = 0

        dsu = DSU(n*m)

        for i in range(n):

            for j in range(m):

                if grid[i][j] == 1:
                    res = max(res,dsu.size[index(i,j)])

                    for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:

                        nr,nc = dr + i, dc + j

                        if nr < 0 or nc <0 or nr >= n or nc >= m or grid[nr][nc] != 1:
                            continue
                        
                        dsu.union(index(nr,nc),index(i,j))
                    res = max(res,dsu.size[dsu.find(index(i,j))])
        return res