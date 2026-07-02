class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        '''
        
        Brute force:
        take small string
        then 
        go through forming substring from it  
        and check if others are divisible.
        '''
        
        res = ""
        resLen = 0
        if len(str1) < len(str2):
            str1,str2 = str2,str1
            
        i = 0
        j = len(str2) -1
        while i <=j :
            substr = str2[i:j+1]
            if self.check(str1,substr) and self.check(str2,substr):
                return substr
            if substr[0] != str1[0] or substr[0] != str2[0]:
                i+=1
            else:
                j-=1
        return "" 
        
    def check(self, s, st):
        
        if len(s)  == 0:
            return True
        if len(st) > len(s):
            return False
        for i in range(len(st)):
            
            if st[i] != s[i]:
                return False
        if len(s) > len(st):
            return self.check(s[len(st):],st)
        return True