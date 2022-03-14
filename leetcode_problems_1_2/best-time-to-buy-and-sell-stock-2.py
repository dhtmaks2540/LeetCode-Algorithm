from typing import List
import sys

class Solution:
    # 브루드 포스로 접근 -> 타임 아웃
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        if len(prices) < 2:
            return max_price

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    # 저점과 고점을 지정하여 풀이
    # 카데인 알고리즘을 응용
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit
        

        
prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))