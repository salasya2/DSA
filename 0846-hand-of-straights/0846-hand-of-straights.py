class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        '''
        hashmap
        '''
        hand.sort()
        freq = defaultdict(int)
        for num in hand:
            freq[num] += 1
        

        for num in hand:
            i = num
            if freq[i] == 0:
                continue
            while  i < num + groupSize:

                if i not in freq:
                    break
                
                i+=1
            if  i == num+groupSize:
                # print(num,"",i)
                # print("----")
                for j in range(num , i):
                    # print(j)
                    freq[j] -= 1
        # print(freq)
        for num in hand:
            if freq[num] != 0:
                return False
        
        return True
        

        