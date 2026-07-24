class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        res = 0

        d = {}
        d[0] = 1
        sums = 0
        for num in nums:
            
            sums += num

            res += d.get(sums - k, 0)

            d[sums] = d.get(sums,0) + 1

        return res