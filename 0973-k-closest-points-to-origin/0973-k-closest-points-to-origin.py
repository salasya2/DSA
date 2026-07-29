class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
        - x,y cords & K
        - K closest points to (0,0) -> distance from (0,0) should be the sorting factor.
        - Euclidean dist -> sqrt((x2**2-x1**2) +(y2**2 - y1**2))
        - answer  -> unique (no mutliple sols)
        - any order is fine

        initial appr ;- go through each point, calculate the distance and push it to the queue along with the distance
        so it must be min_heap -> i can pop the k elements

        '''
        res = []
        max_heap = []

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(max_heap,[-dist,point])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            #[-3,[3,0] , -2 [2,]]
        
        res = [point for _,point in max_heap]
        return res

#O(nlogk),O(k)



