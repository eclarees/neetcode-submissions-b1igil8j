class Solution:
    
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def incrementbyOne(ls):
            # check if ls equals another list that is actly incremental by 1
            return ls==list(range(ls[0],ls[-1]+1))
        hashmap = {}
        for num in hand:
            if num in hashmap:
                hashmap[num] +=1 
            else:
                hashmap[num] =1 
        
        setHand = set(hand)
        sortedHand = list(sorted(setHand))

        actual_num_grps = len(hand)/groupSize
        curgroup = []
        num_grp = 0 
        i=0
        while i<len(sortedHand) and num_grp<actual_num_grps: 
            hashmap[sortedHand[i]]-=1
            curgroup.append(sortedHand[i])
            print(sortedHand[i])
            if hashmap[sortedHand[i]]==0: # remove from set
                sortedHand = sortedHand[:i]+ sortedHand[i+1:]
            else: 
                i+=1 
            print(curgroup)
            print(incrementbyOne(curgroup))
            if len(curgroup)==groupSize and incrementbyOne(curgroup):
                curgroup = [] # reset 
                num_grp +=1 
                print("num grps increased by 1")
                i=0
        if num_grp==actual_num_grps:
            return True
        return False


        
            