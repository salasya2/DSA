class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        '''
        given 

        str with digits -> 2 - 9

        
        '''
        mapping = { '2' : 'abc', '3' : 'def','4':'ghi','5' : 'jkl' , '6' :'mno','7':'pqrs' ,'8':
        'tuv','9' : 'wxyz' }

        res = []
        string = []
        def helper(i):

            if  i == len(digits):
                res.append("".join(string))
                return

            for c in mapping[digits[i]]:
                string.append(c)
                helper(i+1)
                string.pop()

        helper(0)
        return res

        