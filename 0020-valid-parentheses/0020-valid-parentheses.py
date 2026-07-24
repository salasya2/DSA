class Solution:
    def isValid(self, s: str) -> bool:

        d = {'(':')','{':'}','[':']'}

        stack = []

        for i,c in enumerate(s):

            if s[i] in d.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                ch = s[stack.pop()]
                
                if c != d[ch]:
                    return False
        if stack:
            return False
        return True
 
        