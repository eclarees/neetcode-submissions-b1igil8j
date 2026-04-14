class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second>first: 
                diff = second-first
                heapq.heappush(stones, -diff)
        if len(stones)==0:
            return 0 
        else: 
            return abs(stones[0])
                    
