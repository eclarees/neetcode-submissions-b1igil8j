class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones)>1:
            stones.sort() 
            second_heavy, first_heavy = stones[-2],stones[-1]
            if second_heavy==first_heavy:
                stones = stones[:-2] 
            if second_heavy< first_heavy:
                second_heavy = first_heavy - second_heavy 
                stones[-2] = second_heavy
                stones = stones[:-1] 
        if stones:
            return stones[0]
        else:
            return 0
        