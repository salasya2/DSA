class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        freq = {}
        
        for c in s:
            freq[c] = freq.get(c,0) + 1
        
        max_heap = [[-count,c] for c,count in freq.items()]

        res = []
        heapq.heapify(max_heap)
        if -max_heap[0][0] > (len(s) + 1)//2:
            return  ""
        while len(res) < len(s):
            if not max_heap:
                break
            cnt1,c1 = heapq.heappop(max_heap)
            cnt1 = -cnt1 - 1
            res.append(c1)
            if not max_heap:
                break
            cnt2,c2 = heapq.heappop(max_heap)
            cnt2 = -cnt2 - 1
            res.append(c2)
            if cnt1:
                heapq.heappush(max_heap,[-cnt1,c1])
            if cnt2:
                heapq.heappush(max_heap,[-cnt2,c2])
        
        return "".join(res)
            
    # tc :-O(nlogk)   sc:- O(n)
            




        