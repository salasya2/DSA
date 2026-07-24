class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        -> nums and k
        -> k most frequent elements
        -> order doesn't matter
        
        '''
        n = len(nums)
        d = [[]  for  _ in range(n+1)] 
        counter = Counter(nums)
        
        for item,count in counter.items():
            
            d[count].append(item)
        res = []
        target = k
        for i in range(n,-1,-1):

            if  k > 0 and len(d[i]) > 0:
                
                res.extend(d[i])
                k -= len(d[i])
        return res[:target]

        