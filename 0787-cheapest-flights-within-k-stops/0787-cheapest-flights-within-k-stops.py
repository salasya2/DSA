class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        '''
        have to return the flight itineracy with atmost k stops and return -1 if not possible

        brute force - log all the paths, filter  paths with atmost k stops and return cheapest
        '''

        graph = [[] for i in range(n)]

        for u,v, c in flights:
            graph[u].append([v,c])
        
        dist = [[float("inf")] * (k+5) for _ in range(n)]
        dist[src][0] = 0
        min_heap = [[0,0,src]]
        
        while min_heap:

            c,stops,u = heapq.heappop(min_heap)

            if u == dst:
                return c
            if stops == k+1 or dist[u][stops ] < c:
                continue
            
            
            for v,c_v in graph[u]:
                
                nxt_stop = stops + 1
                if c + c_v < dist[v][nxt_stop]:
                    dist[v][nxt_stop ] = c + c_v
                    heapq.heappush(min_heap,[c_v+c,nxt_stop,v])
        return -1 

            