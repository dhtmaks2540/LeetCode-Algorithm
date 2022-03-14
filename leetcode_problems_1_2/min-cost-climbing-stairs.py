from typing import List
import collections


"""
계단은 한 칸이나 두 칸을 오를 수 있는데 계단의 시작 인덱스는 0 또는 1.
꼭대기에 도착하는 최소의 금액을 반환

접근방법

우선 최적 부분 구조인지 파악해보자. 현재까지의 최솟값은 이전 계단의 최솟값 또는 두 칸 전 계단의 최솟값
중 최솟값 + 현재 계단의 값으로 이루어져 있다. 또 이전 계단의 최솟값에다가도 위와 같은 방식으로 구현할 수 있기에
현재 문제의 최선의 값은 부분 문제의 최선의 값으로 이루어져 있어 최적 부분 구조라 할 수 있다.

하위 문제의 중복은 만약 5번째 칸에서의 최솟값을 계산한다면 이는 4번째 칸에서의 최솟값, 3번째 칸에서의 최솟값이 필요하고
또 4번째 칸에서의 최솟값은 3번째 칸에서의 최솟값, 2번째 칸에서의 최솟값이 필요하다. 이와 같이 중복이
발생하기에 DP 테이블을 사용해서 기록하는 다이나믹 프로그래밍으로 문제를 접근할 수 있다.

"""

class Solution:
    # 다이나믹 프로그래밍으로 풀이(상향식)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = collections.defaultdict(int)

        # 첫 번째 칸의 최솟값은 한 칸 오르기
        dp[0] = cost[0]
        # 두 번째 칸의 최솟값은 한 번에 두 칸 오르기
        dp[1] = cost[1]

        for i in range(2, n):
            # 점화식 
            # 현재 위치의 최솟값은 두 번째 이전의 위치 또는 이전 칸 이전의 위치 중 최솟 값 + 
            # 현재 위치의 값
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        # 꼭대기까지 오르는 방법은 이전 위치의 값 또는 두 번째 이전의 위치의 값 중 최솟값
        return min(dp[n - 1], dp[n - 2])

    """
    https://leetcode.com/problems/min-cost-climbing-stairs/discuss/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning
    """

    # 다이나믹 프로그래밍 풀이(하향식)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = collections.defaultdict(int)

        def minCost(n):
            # exit condition
            if n < 0:
                return 0
            
            # 1보다 작으면 한 칸 오르기 또는 두 칸 한번에 오르기
            if n == 0 or n == 1:
                return cost[n]

            if dp[n] != 0:
                return dp[n]

            dp[n] = cost[n] + min(minCost(n - 1), minCost(n - 2))

            return dp[n]

        # 이전의 칸에서 꼭대기까지 한번에 오르기 또는 두 칸 뒤에서 꼭대기까지 한번에 오르기
        return min(minCost(n - 1), minCost(n - 2))

    # optimization
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # 첫 번째 칸, 두 번째 칸
        first = cost[0]
        second = cost[1]

        # 계단의 개수가 2보다 작으면 first와 second의 min 값
        if n <= 2: return min(first, second)

        for i in range(2, n):
            # 현재 위치는 이전 칸, 두 칸 전의 min값 + 현재 위치의 값
            curr = cost[i] + min(first, second)
            # first와 second 갱신
            first = second
            second = curr

        return min(first, second)
    
cost = [10,15,20]
solution = Solution()
print(solution.minCostClimbingStairs(cost))