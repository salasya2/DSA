class DSU:

    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        du = self.find(u)
        dv = self.find(v)

        if du == dv:
            return False
        
        if self.size[du] >= self.size[dv]:
            self.size[du] += self.size[dv]
            self.parent[dv] = du
        
        else:
            self.size[dv] += self.size[du]
            self.parent[du] = dv
        
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        dsu = DSU(n*m)

        def index(r,c):
            return r*m + c
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(m):

                if grid[i][j] == '1':
                    res+=1

                    for dr, dc in directions:
                        nr , nc = i+dr, j + dc

                        if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == '0':
                            continue
                        
                        if dsu.union(index(i,j),index(nr,nc)):
                            res-=1
        
        return res

        