class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        bought = 100000
        total_profit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < bought:
                bought = prices[i]
            elif prices[i] > bought:
                profit = prices[i] - bought
                max_profit = max(max_profit, profit)
                if i == n-1 or prices[i+1] < prices[i]: #end of transaction
                    total_profit += max_profit
                    print("Max profit ", max_profit)
                    print("Total profit ", total_profit)
                    max_profit = 0
                    bought = 100000

        return total_profit