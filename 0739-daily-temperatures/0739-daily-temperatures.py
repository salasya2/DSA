class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
        int list -> temperatures
        return int list -> answer
        answer[i] = no of days after ith day to get temperature[j] > temparature[i]

        i -> check i + 1 to n array
        stack and iterate from the back
        '''
        n = len(temperatures)
        if n == 1:
            return [0]
        answers = [0] * n
        stack = []

        for i in range(n):

            if not stack:
                stack.append(i)
                continue
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    answers[idx] = i - idx
                else:
                    break
            stack.append(i)
        return answers 

        