class Solution:
    def reorganizeString(self, s: str) -> str:

        # a a b
        # a - > 2
        # b - > 1

        # max_heap 
        #[(2,a),(1,b)]
        
        #a add to string # b add to string


        n = len(s)
        freq = {}
        max_freq = 0
        for c in s:
            freq[c] = freq.get(c,0) + 1
            max_freq = max(max_freq,freq[c])
        max_heap = [[-v,k] for k,v in freq.items()]
        heapq.heapify(max_heap)
        res = []

        if max_freq > (len(s) + 1)//2:
            return  ""
        while max_heap:

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




        