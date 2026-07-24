class Solution:
    def firstUniqChar(self, s: str) -> int:

        arr = [0] * 26
        #l - > 1 ,e -> 3, t -> 1 , c -> 1, o -> 1 , d  -> 1
        for c in s:
            arr[ord(c) - ord('a')] += 1
        
        for i,c in enumerate(s):
            
            if arr[ord(c) - ord('a')] == 1:
                return i
        return -1

        