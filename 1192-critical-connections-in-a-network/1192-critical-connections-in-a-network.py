class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = {i : [] for i in range(n)}
        count = set()
        
        rank = [-1]*n
        def dfs(u, depth,parent):
            rank[u] = depth
            for v in graph[u]:

                if v == parent:
                    continue
                if rank[v] == -1:

                    dfs(v,depth + 1,u)
                              
                
                rank[u] = min(rank[u],rank[v])    
                if rank[v] > depth:
                        res.append([u,v]) 
        
        res = []
        for connection in connections:            
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
            
        dfs(0,0,-1)   
        
        return res

        




        