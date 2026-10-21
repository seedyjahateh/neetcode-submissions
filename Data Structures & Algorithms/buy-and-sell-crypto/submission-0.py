class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -float('inf')
        a, b = 0, 0
        while b < len(prices):
            temp = prices[b] - prices[a]
            print(temp)
            if temp > profit:
                profit = temp
            if temp < 0:
                a += 1
            else:
                b += 1

        return profit
            