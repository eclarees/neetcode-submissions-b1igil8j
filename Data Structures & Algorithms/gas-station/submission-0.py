class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # cannot complete loop, if got insufficient gas to cover entire cost
        if sum(gas)<sum(cost):
            return -1 
        
        starting_idx = 0 # store starting index
        total = 0 #track current gas 

        for i in range(len(gas)):
            # at each station i, add the net gas change 
            total += gas[i]-cost[i]
            # if total becomes negative, current starting point cannot work 
            if total<0:
                total = 0 # reset total 
                starting_idx = i+1 # let starting point be next index

        return starting_idx
        