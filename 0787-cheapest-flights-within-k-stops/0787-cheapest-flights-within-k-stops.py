class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n

        prices[src] = 0

        graph = [[] for _ in range(n)]

        for u,v,c in flights:
            graph[u].append([v,c])
        
        q = deque([(0,src,0)])

        while q:
            c,u,stops = q.popleft()

            if stops > k:
                continue
            
            for v,cv in graph[u]:

                next_cost = cv + c

                if next_cost < prices[v]:
                    prices[v] = next_cost
                    q.append((next_cost,v,stops+1))
        
        return prices[dst] if prices[dst]!= float("inf") else -1