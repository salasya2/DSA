class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        flag = {0 : False,1:False,2:False}

        for triplet in triplets:

            if target[0] < triplet[0] or target[1] < triplet[1] or target[2] < triplet[2]:
                continue
            
            if target[0] == triplet[0]:
                flag[0] = True
            if target[1] == triplet[1]:
                flag[1] = True
            if target[2] == triplet[2]:
                flag[2] = True

            if all(flag.values()):
                return True


        return False