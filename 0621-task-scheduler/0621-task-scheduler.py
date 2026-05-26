
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        max_heap = [val for val in count.values()]
        heapq.heapify_max(max_heap)
        queue = deque([])

        time = 0

        while max_heap or queue:

            time+=1

            if not max_heap:
                time = queue[0][1]

            else:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt:
                    queue.append([cnt, time + n])
                
            if queue and time == queue[0][1]:

                cnt, time = queue.popleft()
                heapq.heappush_max(max_heap, cnt)
            
        return time


