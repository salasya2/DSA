class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        arr = [0]*26

        for i,c in enumerate(s):
            arr[ord(c) - ord('a')] = i
        # x - 3, y - 4, z -7,b-9,i-10,s-11,l-12
        end = 0
        start = 0
        res = [] 
        for i in range(len(s)):
            c = s[i]
            if i > end:
                res.append(end-start+1)
                end = arr[ord(c)-ord('a')]
                start = i
            
            else:
                end = max(end,arr[ord(c)-ord('a')])
        res.append(end-start+1)
        return res        