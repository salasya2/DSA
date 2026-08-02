class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        n = len(gas)  
        if sum(gas) < sum(cost):
            return -1
        # start = []
        # for i in range(len(gas)):

        #     if gas[i] >= cost[i]:
        #         start.append(i)
        
        # for i in start:
        #     tank = gas[i]
        #     idx = i
        #     tank -= cost[idx]
        #     idx = (idx + 1) % n
            
        #     while tank + gas[idx]>= cost[idx]:
        #         tank = tank + gas[idx] - cost[idx]
        #         if idx == i:
        #             return i
        #         idx = (idx + 1)%n

        res = 0
        current_tank  = 0
        for i in range(n):

            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                res = i + 1
                current_tank = 0
        return res


        