class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        
        count1 = [0]* 26
        count2 = [0]* 26

        for i in range(len(s1)):

            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        

        i  = 0

        matches = 0

        for j in range(26):

            if count1[j] == count2[j]:
                matches+=1
        
        for j in range(len(s1),len(s2)):

            if matches == 26:
                return True


            index = ord(s2[j]) - ord('a')

            count2[index] += 1

            if count2[index] == count1[index]:
                matches += 1

            elif count1[index] + 1 ==  count2[index] :
                matches -= 1


            index = ord(s2[i]) - ord('a')

            count2[index] -= 1

            if count2[index] == count1[index]:
                matches+=1
            
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            
            i+=1
        
        return (matches == 26)





            


        