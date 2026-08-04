class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = Counter(nums)
        n = len(nums)
        for num,c in counter.items():
            if c > math.floor(n/2):
                return num
        
        return nums[0]


        