class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        s = ""

        
        def dfs(s,Open,closed):
            if n * 2 == len(s):
                res.append(s)
                return
            
            if Open < n:
                
                dfs(s +"(", Open+1, closed)
                
            
            if closed < Open:
                
                dfs(s + ")", Open,closed+1)
                

            

        dfs(s,0,0)
        return res        