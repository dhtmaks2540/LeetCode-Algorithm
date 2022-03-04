from typing import List
import sys

class Solution:
    # 카데인 알고리즘 응용
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = sys.maxsize
        max_value = -1

        for num in nums:
            # 최솟값
            min_value = min(min_value, num)
            # 현재값 - 최솟값이 최댓값이 되도록 계속 갱신
            max_value = max(max_value, num - min_value)
        
        # 0이면 최댓값이 계속 0이였다는 뜻이므로 -1 반환
        if max_value == 0:
            return -1
        
        return max_value

    def maximumDifference(self, nums: List[int]) -> int:
        diff, mi = -1, sys.maxsize
        for i, n in enumerate(nums):
            # i가 0보다 크도 현재값이 최솟값보다 작을 때
            if i > 0 and n > mi:
                # 현재값 - 최솟값을 최댓값으로 갱신
                diff = max(diff, n - mi)

            # 최솟값 갱신
            mi = min(mi, n)

        return diff

nums = [9, 4, 3, 2]
solution = Solution()
print(solution.maximumDifference(nums))