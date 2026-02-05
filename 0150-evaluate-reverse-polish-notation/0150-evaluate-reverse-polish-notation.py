
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i,c in enumerate(tokens):

            if c not in "+-*/":
                stack.append(c)

            else:

                a = int(stack.pop())
                b = int(stack.pop())

                if c == '+':

                    res = a + b
                elif  c == '-':
                    res = b - a

                elif c == '*':
                    res = a * b

                elif c == '/':
                    res = int(b/a)

                stack.append(res)

            # print(stack)
        return int(stack.pop())
        

        
        
                

        