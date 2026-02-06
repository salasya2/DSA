class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            if stack:

                index = stack[-1]
                if temperatures[i] < temperatures[index]:
                    stack.append(i)
                    continue
                
                else:

                    while stack and temperatures[stack[-1]] < temperatures[i]:

                        index = stack.pop()

                        res[index] = i - index

            stack.append(i)

        return res



            



