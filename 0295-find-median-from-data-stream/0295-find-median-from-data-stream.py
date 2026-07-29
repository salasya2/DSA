class MedianFinder:

    def __init__(self):
        
        self.min_heap = []
        self.max_heap = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)

        ele = heapq.heappop(self.max_heap)

        heapq.heappush(self.min_heap,-ele)

        if len(self.min_heap) != len(self.max_heap):
            ele = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-ele)

    def findMedian(self) -> float:
        total_len = len(self.min_heap) + len(self.max_heap)

        if total_len % 2:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2.0

#O (logn) O(n)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()