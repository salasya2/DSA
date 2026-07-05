class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        bfs


        '''

        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append([v,t])
        
        visited = [[0,k]]
        seen = set()
        t = 0
        heapq.heapify(visited)
        while visited:
            time,node = heapq.heappop(visited)
           
            if node in seen:
                continue
            seen.add(node)
            t = time
            for v,t1 in graph[node]:
                
                if v not in seen:
    
                    
                    heapq.heappush(visited,[t+t1,v])
        
        if len(seen) != n:
            return -1
        return t
            


