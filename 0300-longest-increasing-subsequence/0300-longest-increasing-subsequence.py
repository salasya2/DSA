class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []

        for num in nums:
            l = 0
            h = len(sub) - 1

            while l <= h:
                m = l + (h - l)//2
                if sub[m] < num:

                    l = m + 1
                else:
                    h = m - 1
            
            if l == len(sub):
                sub.append(num)
            else:
                sub[l] = num
        
        return len(sub)