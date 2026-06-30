class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        
        i have a string and have to count the number of palindromes in s.

        bruteforce will:

        two loops to computer the substring
        and third loop to check if palindrome or not..
        O(n^3) time and O(1) auxiliary space

        DP:
        dp = [[false]*n for _ in range(n)]

        dp[i][j] = True -> palindrome

        populate dp first and then check for total number
        
        o(n^2) and o(n^2)

        Two pointers:

        go to each index and use that index as center of palindrome and expand to other sides

        check for odd len palindromes and even len palindromes.
    
        '''

        n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # res = 0

        # for i in range(n-1,-1,-1):

        #     for j in range(i,n):

        #         if s[j] == s[i] and (j -i <=2 or dp[i+1][j-1] == True):
        #             dp[i][j] = True
        #             res += 1
        
        res = 0

        for i in range(n):

            l , h = i , i 

            while l >=0 and h <= n-1 and s[l] == s[h]:
                l -= 1
                h += 1
                res+=1
            
            l , h = i, i+1
            while l >= 0 and h <= n-1 and s[l] == s[h]:
                l -= 1
                h += 1
                res += 1

        return res
