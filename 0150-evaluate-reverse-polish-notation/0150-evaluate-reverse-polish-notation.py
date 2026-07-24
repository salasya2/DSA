class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        n = len(tokens)

        for c in tokens:

            if c not in ('+','-','*','/'):
                stack.append(int(c))
                continue
            
            num2 = stack.pop()
            num1 = stack.pop()

            match c:
                case "+":
                    num = num1 + num2
                    if num > 2**31-1:
                        num = 2**31-1
                    stack.append(num1+num2)
                case '-':
                    num = num1 - num2
                    if num < -2**31:
                        num = -2**31
                    
                    stack.append(num)
                case '*':
                    num = num1 * num2
                    if num > 2**31-1:
                        num = 2**31-1
                    if num < -2**31:
                        num = - 2 ** 31
                    stack.append(num)
                case '/':
                    num = math.trunc(num1/num2)
                    if num > 2**31-1:
                        num = 2**31-1
                    if num < -2**31:
                        num = - 2 ** 31
                    stack.append(num)

        return stack[-1]

        