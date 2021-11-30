import sys

# 브루드 포스(타임아웃)
def maxProfit(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# 카데인 알고리즘 응용
def maxProfit(prices):
    # 최댓값
    profit = 0
    # 최솟값
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    # 최저점과 최고점을 찾는 방식
    for i, price in enumerate(prices):
        min_price = min(min_price, price)

        profit = max(price - min_price, profit)

    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))