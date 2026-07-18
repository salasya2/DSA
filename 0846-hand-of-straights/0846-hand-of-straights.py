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
            start = num
            while freq[start-1]:
                start -= 1
            while  start <= num:
                while freq[start]:

                    for i in range(start,start+groupSize):
                        if not freq[i]:
                            return False
                        freq[i] -= 1   
                start += 1
                
            
        return True
        

        