class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        

        #o(n^3), o(n)
        nums.sort()
        n = len(nums)
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            h = n - 1

            while l<h:

                Sum = nums[i] + nums[l] + nums[h]
                
                if Sum < 0:
                    l += 1

                elif Sum > 0:
                    h -= 1

                else:
                    res.append([nums[i],nums[l],nums[h]]) 
                    l += 1
                    h -= 1

                    while (l<h and nums[l] == nums[l - 1]): l+=1
                    while (l <h and nums[h] == nums[h+1]): h -= 1

        return res