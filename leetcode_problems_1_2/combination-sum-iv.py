from dis import dis
from typing import List

"""
이 문제와 비슷함
https://leetcode.com/problems/coin-change-2/description/
"""

class Solution:
    """
    https://leetcode.com/problems/combination-sum-iv/discuss/111860/Coin-change-AND-this-problem
    """
    # DP로 접근 -> 점화식 생각해야함
    # 코인 문제는 1 + 1 + 2와 1 + 2 + 1을 같은 값으로 계산하지만
    # 이 문제는 다른 값으로 계산해야 하기에 for loop가 다르다.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp 테이블
        dp = [0] * (target + 1)
        # 첫 번째 원소는 1로
        dp[0] = 1

        # dp 테이블을 이터레이션하며
        for i in range(1, target + 1):
            # nums리스트의 숫자를 이터레이션
            for n in nums:
                # i의 값이 n보다 크거나 같다면
                if i >= n:
                    # dp[i] += dp[i - n]
                    dp[i] += dp[i - n]

        return dp[target]

    """
    https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question
    """
    # DP로 접근
    def combinationSum4(self, nums, target):
        # 정렬 수행한 nums와 dp 테이블(첫 번째 인자는 1)
        nums, combs = sorted(nums), [1] + [0] * (target)
        # target 이터레이션
        for i in range(target + 1):
            # 리스트 이터레이션
            for num in nums:
                # 현재의 값이 target보다 크다면 break(정렬되어 있으므로)
                if num  > i: break
                # num이 target과 같으면 새로운 조합 생성
                # num이 target보다 작으면 현재의 target에서 num값을 뺀 dp 테이블 값 가져오기
                combs[i] += combs[i - num]
        return combs[target]

nums = [1,2,3]
target = 4
solution = Solution()
print(solution.combinationSum4(nums, target))