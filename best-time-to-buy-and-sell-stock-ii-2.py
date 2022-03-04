from typing import List

# 여러번의 거래로 낼 수 있는 최대 이익을 산출
class Solution:
    """
    그리디 알고리즘으로 문제 풀이

    1. 이후의 결과는 상관하지않고 현재 최적의 답을 도출(값이 오르는 경우 판다) -> 아이디어에 해당

    2. 산날 바로 살 수 있기에 오르기전에 사고 내리기전에 판다는 방식으로 접근
    예를 들어, [1,2,3,4,5]와 같은 경우 1에 구매해서 5에 판다는 개념은
    1에 구매 - 2에 판매, 2에 구매 - 3에 판매, 3에 구매 - 4에 판매, 4에 구매 - 5에 판다라는 개념과 똑같다.
    따라서 위의 아이디어를 사용해 문제 풀이가 가능
    """
    # 값이 내리기 전에 팔고, 오르기 전에 사면 됨
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result

    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me.
    
    The buying at day i, selling at day j, The range[i, j] should be chosen so that sub-profit is maximum

    sub-profit = prices[j] - prices[i]

    We should choose j that prices[j] is as big as possible, and choose i that prices[i] is
    as small as possible.

    From this observation, from day X, the buying day will be the last continuous day that price is smallest.
    Then, the selling day will be the last continuous day that the price is biggest.

    """
    def maxProfit(self, prices: List[int]) -> int:
        # 사는날, 파는날, 이익 변수
        buy = sell = profit = 0
        i , n = 0, len(prices) - 1

        while i < n:
            # 다음 값이 현재의 값보다 작거나 같은 동안에(연속된 값중 가장 작은 값 찾기 -> 큰 값이 발견되면 중단)
            while i < n and prices[i + 1] <= prices[i]: i += 1
            buy = prices[i]

            # 다음 값이 현재의 값보다 큰 동안에(연속된 값중 가장 큰 값 찾기 -> 작은 값이 발견되면 중단)
            while i < n and prices[i + 1] > prices[i]: i += 1
            sell = prices[i]

            # 현재의 값 계산
            profit += sell - buy

        return profit

    # 사는날, 파는날 날짜 구하기
    def maxProfit(self, prices: List[int]) -> List:
        i, n = 0, len(prices) - 1
        i_buy = i_sell = profit = 0
        buy_and_sells = []

        while i < n:
            while i < n and prices[i + 1] <= prices[i]: i += 1
            i_buy = i

            while i < n and prices[i + 1] > prices[i]: i += 1
            i_sell = i

            profit += prices[i_sell] - prices[i_buy]
            buy_and_sells.append((i_buy, i_sell))

        return buy_and_sells

    """
    DP로 문제 풀이
    i번째 날짜에 할 수 있는 것은 buy(마지막 action이 sell이라면), 또는 sell(마지막 action이 buy라면)
    또는 아무것도 안하기(사지도 팔지도 않는다)이다.

    각 반복에 있어서 아래와 같은 선택을 한다.
    1. 아무것도 안하기 = lastBuy or lastSold(가진 돈의 변화가 없게 유지하기에)
    2. 이익을 가지고 팔기 = lastBuy + current(증가한 금액만큼 팔기 때문에)
    3. 새로운 주식을 사기 = lastSold - current
    (주식을 사기 위해 돈이 필요하기 때문에 새로운 주식을 사기 위해 이익을 팔아야 한다)

    위의 선택에 있어서
    curBuy는 주식을 사야 하는지를 결정하는 것으로, 이미 매입한 것과 이전 수익을 포기해 현재 주식을
    사는 것의 최대값

    cursell은 주식을 팔지를 경정하는 것으로, 기존 이익(마지막 매도)과 현재 주식을 매도하는 것의 최대치
    """
    def maxProfit(self, prices: List[int]) -> List:
        n = len(prices)
        last_buy, last_sold = -prices[0], 0

        for i in range(n):
            cur_buy = max(last_buy, last_sold - prices[i])
            cur_sold = max(last_sold, last_buy + prices[i])
            last_buy = cur_buy
            last_sold = cur_sold

        return last_sold

prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))