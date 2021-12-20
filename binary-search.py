from typing import List
import bisect


class Solution:
    # 반목문으로 이진 탐색 구현
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        # start가 end보다 작거나 같은 동안에
        while start <= end:
            # 중앙 값 계산
            mid = start + (end - start) // 2
            # 같다면 반환
            if nums[mid] == target:
                return mid
            # 크다면 end 줄이기
            elif nums[mid] > target:
                end = mid - 1
            # 작다면 start 늘리기
            else:
                start = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        # 이진 탐색 재귀
        def binary_search(start, end):
            if start > end:
                return -1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)

        start = 0
        end = len(nums) - 1

        return binary_search(start, end)

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return -1

    # 재귀 풀이 책 정답
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                return mid
            else:
                return -1
        
        return binary_search(0, len(nums) - 1)

    # 이진 검색 모듈
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    # index()를 이용한 풀이
    def search(self, nums: List[int], target: int) -> int:
        # index() 메소드는 존재하지 않는 값이면 에러를 발생
        # 그 에러를 예외 처리
        try:
            return nums.index(target)
        except ValueError:
            return -1