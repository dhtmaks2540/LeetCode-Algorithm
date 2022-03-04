from typing import List

import collections

class Solution:
    # 상향식 풀이
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        if len(nums) <= 2:
            return max(nums)

        # 첫 번째 집을 털 경우
        dp[1] = nums[0]
        # 첫 번째 집과 두 번째 집의 max값
        dp[2] = max(nums[0], nums[1])

        for i in range(3, len(nums) + 1):
            # 이전의 집을 털 경우와 두 번째 전의 집을 털고 현재 집을 턴 경우
            # 위의 두 경우중 최댓값을 저장
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]

    # 브루드포스로 풀이(타임아웃)
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0

            return max(_rob(i - 1), _rob(i - 2) + nums[i])
        return _rob(len(nums) - 1)

    # 타뷸레이션
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]

nums = [2, 1, 1, 2]
solution = Solution()
print(solution.rob(nums))