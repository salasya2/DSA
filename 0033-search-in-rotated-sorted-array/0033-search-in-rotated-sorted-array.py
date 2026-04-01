class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l , r = 0, len(nums)-1
        pivot = 0
        while l < r :

            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l

        l, r = 0 , len(nums) - 1
        # print(pivot, nums[pivot])
        if target>= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r :

            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    
        