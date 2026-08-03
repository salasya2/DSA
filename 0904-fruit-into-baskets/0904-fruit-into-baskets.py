class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        

        n = len(fruits)

        '''
        
        1 , 2, 1, 2, 3 , 3

        3 -> 2
        2 -> 2
        1 -> 2
        
        
        '''

        i = 0
        j = 0
        res = 0
        seen = {}
        # 1, 2 , 3, 2, 4
        while i < n and j < n:

            if len(seen) == 2 and fruits[j] not in seen:
               
                idx = j
                for fr,fruit_id in seen.items():
                    idx = min(fruit_id,idx)
                start = fruits[idx]
                i = idx + 1
                del seen[start]

            seen[fruits[j]] = j
            res = max(res,j - i + 1)
            j += 1
            
        # res = max(res,j - i)
        return res



