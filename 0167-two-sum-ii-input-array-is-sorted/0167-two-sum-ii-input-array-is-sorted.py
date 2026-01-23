class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        res = []

        i = 0 
        j = len(numbers)-1

        while(i<=j):

            if numbers[i] + numbers[j] == target and i!=j:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
        
        return res

        