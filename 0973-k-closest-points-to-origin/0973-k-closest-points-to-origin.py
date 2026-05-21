class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result = []

        for x , y in points:

            dist = math.sqrt(x**2 + y**2)

            heapq.heappush_max(result,[dist,x,y])


            if len(result) > k:
                heapq.heappop_max(result)
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop_max(result)
            res.append([x,y])
        return res

        