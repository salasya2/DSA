class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num2alph = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

        if len(digits) == 0:
            return []
        res = []

        def dfs(subset,i):
            

            if i >= len(digits):

                res.append(subset)
                return
            alphs = num2alph[digits[i]]
            
            for j in alphs:

                dfs(subset+j,i+1)

        dfs("",0)
        return res
