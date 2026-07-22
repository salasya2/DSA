class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

        n = len(s)
        maxLen = 0
        if n == 0:
            return 0

        hashMap = defaultdict(int)
        end = 0
        while  end < n and hashMap[s[end]] == 0:
            hashMap[s[end]] += 1 
            maxLen += 1
            end += 1
        start = 0
        print(end,maxLen)
        for i in range(end,n):

            if hashMap[s[i]] != 0:
                
                while hashMap[s[i]] != 0:
                    hashMap[s[start]] -= 1
                    start += 1
                hashMap[s[i]] += 1
            else:
                
                hashMap[s[i]]+=1
                maxLen = max(i-start+1,maxLen)
        
        return maxLen

        