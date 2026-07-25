class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        l = 0 

        h = n - 1
        if  n == 1:
            if nums[l] == target:
                return l
            return -1

        while l <= h:

            mid = l + (h - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[h]:

                if target > nums[h] and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1 

            else:
                if target <= nums[h] and target > nums[mid]:
                    l = mid +1
                else:
                    h = mid - 1
        return -1
                

        
        return -1



        