# Last updated: 5/25/2025, 1:08:26 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find biggest positive differential in the list
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
        # need to parse through list and get the biggest positive differential between values
    #    buyDay = 0
    #     sellDay = 0
    #     profit = 0
    #     for i in range(len(prices)):
    #         for j in range(i, len(prices)):
    #             if i!= j:
    #                 if (prices[j] - prices[i]) > profit:
    #                     buyDay = i
    #                     sellDay = j
    #                     profit = prices[j] - prices[i]
    #                     # print(i, j, prices[i], prices[j], profit)
    #     return profit 

    # def maxProfit(self, prices: List[int]) -> int:
    #     min_price = prices[0]
    #     max_profit = 0
        
    #     for price in prices[1:]:
    #         print(price)
    #         max_profit = max(max_profit, price - min_price)
    #         min_price = min(min_price, price)
            
    #     return max_profit
        