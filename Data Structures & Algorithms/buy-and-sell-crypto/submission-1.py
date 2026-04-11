class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 

        for i in range(1,len(prices)): 
            minPrice = min(prices[:i])
            sellingPrice = prices[i]
            
            profit = sellingPrice-minPrice 
            maxProfit = max(profit,maxProfit)
        return maxProfit
            



        