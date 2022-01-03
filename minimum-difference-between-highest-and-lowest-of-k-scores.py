from typing import List
import sys

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 예외처리
        if len(nums) == 1 or k == 1:
            return 0

        # 정렬
        nums.sort()

        minimum_value = sys.maxsize
        left, right = 0, k - 1

        # 범위안에서 이터레이션
        for i in range(len(nums) - k + 1):
            minimum_value = min(minimum_value, (nums[right] - nums[left]))
            left += 1
            right += 1

        return minimum_value

    def minimumDifference(self, nums: List[int], k: int) -> int:
        return min(y - x for x, y in zip(sorted(nums)[:-k + 1], sorted(nums)[k - 1:])) if k > 1 else 0

nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
solution = Solution()
print(solution.minimumDifference(nums, k))