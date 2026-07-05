class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #BRUTE FORCE
        # m=0
        # for i in range(len(prices)):
        #     for j in range(i+1,(len(prices))):
        #         if prices[i]<=prices[j]:
        #             m = max(m,prices[j]-prices[i])
        # return m
        min_price = prices[0] # this will check any price which could be minimum so that profit should be maximized because by subtracting the smallest number from another number will create maximum profit. Thus we are keeping the pointer for min price
        max_profit = 0
        for price in prices:
            if min_price> price:#at any point if there is some value which is smaller than previous value, we are going to keep it
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit