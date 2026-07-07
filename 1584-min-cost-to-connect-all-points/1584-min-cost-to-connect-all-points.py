class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = 0
        node = 0
        visited = [False] * n
        res = 0
        dist = [100000000] * n
        
        while edges < n-1:

            visited[node] = True
            nextnode = -1
            for i in range(n):

                if visited[i]:
                    continue
                
                curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(curDist,dist[i])
                if nextnode == -1 or dist[i] < dist[nextnode]:
                    nextnode = i
            res += dist[nextnode]
            node = nextnode
            edges += 1
        
        return res