class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        res = 0
        count = {}
        max_element = 0

        i = 0

        for j in range(n):

            

            count[s[j]] = 1 + count.get(s[j],0)

            max_element = max(max_element, count[s[j]])

            if k + max_element >= j - i + 1:
                res = max(res, j-i+1)
            else:
                
                if max_element == count[s[i]]:
                    max_element -=1
                count[s[i]] -= 1
                i+=1
            

        return res

                    

        