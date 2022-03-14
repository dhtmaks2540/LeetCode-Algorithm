from typing import List
import sys

class Solution:
    # 여행일자를 모두 커버하는 티켓의 최소 금액
    # 재귀 구조로 풀이 -> 시간 초과
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c \
                    # zip 함수를 사용하여 costs와 duration 묶기
                    for c, d in zip(costs, durations))
            else:
                return dp(i + 1)
        
        return dp(1)

    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # 가장 긴 day 범위까지 0으로 초기화
        dp=[0 for i in range(days[-1]+1)]
        for i in range(days[-1]+1):
            # 해당 날짜가 days에 없다면
            if i not in days:
                # 하루전과 일치
                dp[i]=dp[i-1]
            # 있다면
            else:
                # 7일전, 1일전, 30일전 중 가장 작은 값 가져오기
                dp[i]=min(dp[max(0,i-7)]+costs[1],dp[max(0,i-1)]+costs[0],dp[max(0,i-30)]+costs[2])
        return dp[-1]
                
days = [1,4,6,7,8,20]
costs = [2,7,15]

solution = Solution()
print(solution.mincostTickets(days, costs))