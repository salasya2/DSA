class MedianFinder:

    def __init__(self):
        self.minHeap =[ ]
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap,num)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            element = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap,element)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            element = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap,element)
        # print(self.maxHeap,self.minHeap)
        

    def findMedian(self) -> float:
        

        total_len = len(self.minHeap) + len(self.maxHeap)
        res = 0.0
        if total_len%2 == 0:
            maxEle = self.maxHeap[0]
            minEle = self.minHeap[0]
            return (minEle+maxEle)/2.0
        
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        return self.minHeap[0]
        
        