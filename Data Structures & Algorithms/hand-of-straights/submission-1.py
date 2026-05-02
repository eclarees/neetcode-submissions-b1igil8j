class Solution:
    
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # create a hashmap, counting the frequency of each card 
        hashmap = {}
        for card in hand:
            hashmap[card] = hashmap.get(card,0)+1 

        for card in sorted(hashmap):
            start = card 
            while hashmap[card] > 0:
                for num in range(start,start+groupSize):
                    if num not in hashmap or hashmap[num]==0:
                        return False
                    
                    hashmap[num]-=1 
        return True