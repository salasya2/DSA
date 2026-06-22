class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # check for any element appearing twice

        #initial approach is to use hash table and if i find entry inc to 2, return true
        # sorting the list to find the duplicates

        nums.sort()

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:
                return True
            
        return False

        