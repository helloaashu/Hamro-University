"""LeetCode 121: Best Time to Buy and Sell Stock"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Max profit:", Solution().maxProfit(prices))
