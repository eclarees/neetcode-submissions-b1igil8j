class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1,len(dp)):
            # eg. i = 5 (amount 5)
            if i in coins:
                dp[i]=1
            else:
                # iterate through the coins avail
                for coin in coins: 
                    if coin<i: #eg. coin = 3 
                        # 1+dp[i-coin]: means use the coin and use dp of remaining (i-coin)
                        dp[i] = min(dp[i],1+dp[i-coin])

        if dp[-1]==float('inf'):
            return -1
        return dp[-1]


        