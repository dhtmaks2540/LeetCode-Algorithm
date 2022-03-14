from typing import List
import collections

"""
인접한 집을 털면 안된다는 제약조건이 있을 때 돈을 최대로 털 수 있는 값을 반환

접근방법

우선, 현재 문제가 최적 부분 구조인지 먼저 파악하자.
최적 부분 구조는 현재 문제의 최선의 답은 부분 문제의 최선의 답으로 이루어져있다인데
만약 4번째 집을 가정하고 돈을 최대로 터는 방법은
2번째 집을 털고 현재 집을 털거나 3번째 집을 터는 방법 중 최댓값을 구하는 방법으로 이루어져 있다.
따라서 현재 문제의 최선의 답이 부분 문제의 최선의 답으로 이루어져 있기에 최적 부분 구조에 해당한다.

그리고 다이나믹 프로그래밍의 가장 중요한 조건에 해당하는 하위 문제의 중복은
dp[5] = dp[3] + nums[5] or dp[4] / dp[4] = dp[2] + nums[4] or dp[3]과 같이 발생하기에
DP 테이블을 이용해서 이 값을 기록하기 위해 다이나믹 프로그래밍으로 문제를 접근한다.
"""

class Solution:
    # 다이나믹 프로그래밍으로 문제 풀이(상향식)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # DP 테이블
        dp = collections.defaultdict(int)

        for i in range(n):
            if i < 2: dp[i] = nums[i]
            # 점화식
            # 현재 위치에서 최대로 집을 터는 방법은
            # 현재 위치에서 두 번째 이전의 위치를 털고 현재 위치를 터는 방법
            # 또는 이전 위치를 턴 방법 중 최댓값에 해당한다.
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]

    # 재귀구조로 접근
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def maxCost(n):
            # exit condition
            if n < 0: return 0
            # n의 길이가 0 또는 1이라면 
            if n == 0 or n == 1: return nums[n]
            # 점화식에 해당
            # 두개 이전의 위치 최댓값 + 현재 위치의 값 또는 한개 이전의 위치의 최댓값 중 최댓값
            return max(maxCost(n - 2) + nums[n], maxCost(n - 1))

        return maxCost(n - 1)

    # 책의 정답(다이나믹 프로그래밍 상향식 = 타뷸레이션)
    def rob(self, nums: List[int]) -> int:
        # exit condition
        if not nums:
            return 0
        # 2개 이하라면 max값 반환
        if len(nums) <= 2:
            return max(nums)

        # 순서를 유지하는 dict
        dp = collections.OrderedDict()
        # 첫 번째 집을 터는 방법은 하나
        # 두 번째 집을 터는 방법은 첫 번째 집 혹은 두 번째 집 중 최댓값
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # 점화식에 해당
            # 두개 이전 위치의 최댓값 + 현재 위치지 집 또는 한개 이전 위치의 최댓값 중 최댓값
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp.popitem()[1]

    # 다이나믹 프로그래밍(탑다운 = 메모제이션) -> 시간초과
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        def _rob(n):
            if n < 0:
                return 0

            if dp[n] != 0:
                return dp[n]

            dp[n] = max(_rob(n - 2) + nums[n], _rob(n - 1))
            return dp[n]

        return _rob(len(nums) - 1)
        
nums = [2,7,9,3,1]
# nums = [1,2,3,1]
solution = Solution()
print(solution.rob(nums))