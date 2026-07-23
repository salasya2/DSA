class Solution:
    def trap(self, height: List[int]) -> int:


        n = len(height)

        if not height:
            return 0


        res = 0

        leftMax = 0
        rightMax = 0

        i = 0
        j = n - 1

        while i < j:
            

            leftMax = max(leftMax,height[i])
            rightMax = max(rightMax,height[j])
            if leftMax < rightMax:
                res += max(0,leftMax - height[i])
                i += 1
            else:
                res += max(0,rightMax - height[j])
                j -= 1
        return res
            

        