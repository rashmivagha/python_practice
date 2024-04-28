class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        bought = prices[0]
        total_profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < bought:
                bought = prices[i]
            elif prices[i] > bought:
                profit = prices[i] - bought
                if profit > max_profit:
                    max_profit = profit
                    if i == n-1 and total_profit == 0:
                        total_profit = max_profit
                else:
                    total_profit += max_profit
                    print("Max profit ", max_profit)
                    print("Total profit ", total_profit)
                    max_profit = 0
                    bought = prices[i]

        return total_profit