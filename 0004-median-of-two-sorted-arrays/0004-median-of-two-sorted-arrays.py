class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        #  1, 2 ,3
        #  4, 5, 6
        #  total - 6, half = 3
        #
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        half = total//2
        l = 0
        h = len(nums1) - 1
        while True:

            i = l + (h - l)//2
            j = half - i - 1 - 1

            Aleft = nums1[i] if i >= 0 else float("-inf")
            Aright = nums1[i+1] if  i+1<len(nums1) else float("inf")
            Bleft = nums2[j] if j >= 0 else float("-inf")
            Bright = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total %2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright) )/ 2.0
            elif Aleft > Bright:
                h = i - 1
            
            else:
                l = i + 1
        return  0.0