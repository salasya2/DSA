class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        d = {'(':')','{':'}','[':']'}

        for c in s:

            if c == '(' or c=='{' or c == '[':
                stack.append(c)
            
            elif c == ')' or c == '}' or c ==']':

                if len(stack)==0:
                    return False
                cl = stack.pop()

                if d[cl] != c:
                    return False
        
        return (len(stack) == 0)