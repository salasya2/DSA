class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        -> nums and k
        -> k most frequent elements
        -> order doesn't matter
        
        '''

        d = {}

        for num in nums:
            d[num] = d.get(num,0) + 1

        sortedDict = sorted(d.items(), key = lambda x : (x[1],x[0]),reverse = True)
        res = []
        for  i in range(k):

            res.append(sortedDict[i][0])
        return res
        