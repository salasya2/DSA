class Solution:
    def numDecodings(self, s: str) -> int:
        

        '''
        - number in string -> try to decode the way - > matching numbers to letter

        - 06 is not valid
        
        226 => 

        0<i<2 if i == 2 then i+1 < 7
         if decode of rest is successful -> then 2 ways

        s[i:]

        '''
        res = 0 
        dp1 = 0 
        dp2 = 1
        n = len(s)
        curr = 0
        for i in range(n):

            
            curr = 0
            if s[i]!="0":
                curr +=  dp2  
            if i>0 and ( s[i-1] == "1" or (s[i-1] == "2" and s[i] < "7")):
                curr += dp1
                    
            
            dp1 = dp2
            dp2 = curr
                
        return dp2
                
                


                



        # n = len(s)
        # def helper(i):
        #     nonlocal res,n

        #     if i == n:
        #         return 1
            
        #     if s[i] == "0":
        #         return 0
            
        #     res = helper(i+1)
        #     if i < n - 1:
        #         if s[i] == "1" or s[i] == "2" and s[i+1] < "7":
        #             res += helper(i+2)
        #     return res
        # return helper(0)
        