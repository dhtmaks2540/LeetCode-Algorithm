from typing import List

import bisect


class Solution:
    # 이진 탐색 활용
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            # 현재 값 빼기
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

    # 투 포인터를 활용
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while not i == j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return i + 1, j + 1 # 리턴 값 + 1

    # bisect 모듈과 슬라이싱을 활용
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            
            if i < len(numbers[k+1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2

    # bisect 모듈과 슬라이싱 최소화
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2

    # bisect 모듈과 슬라이싱 제거
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            # 왼쪽 범위 제한(bisect.bisect_left(a, x, lo = 0, hi = len(a))) -> 왼쪽 범위, 오른쪽 범위 파라미터
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


numbers = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(numbers, target))