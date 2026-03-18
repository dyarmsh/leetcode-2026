from typing import List

"""
[EASY] BEST TIME TO BUY AND SELL STOCK
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Date: 18th March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(prices)
    - looking at each element at most once
    - using a two pointer approach
Space: O(1)
    - comparisons performed in-place
"""

def maxProfit(prices: List[int]) -> int:
    buy = 0
    sell = 1

    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1


    return max_profit
        