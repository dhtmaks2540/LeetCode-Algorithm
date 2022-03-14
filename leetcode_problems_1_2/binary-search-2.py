from re import M
from typing import List
import bisect

# use binary search to find target in nums
class Solution:
    """
    이진 탐색은 시간 복잡도가 O(logn)으로 원하는 값을 찾는 알고리즘이다.
    다만, 이진 탐색은 배열이 정렬되어 있는 경우에만 수행이 가능한 알고리즘이다.
    """
    # 반복문
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # exit condition
        while left <= right:
            # mid index
            mid = (left + right) // 2

            # find target
            if nums[mid] == target:
                return mid
            # target보다 큰 경우는 right 값을 mid - 1로
            elif nums[mid] > target:
                right = mid - 1
            # target보다 작은 경우는 left 값을 mid + 1로
            else:
                left = mid + 1

        # 못 찾은 경우
        return -1

    # 재귀구조
    def search(self, nums: List[int], target: int) -> int:
        def find_target(left, right):
            # exit condition
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return find_target(left, mid - 1)
            else:
                return find_target(mid + 1, right)

        return find_target(0, len(nums) - 1)

    # 이진 탐색 모듈(bisect)을 사용
    def search(self, nums: List[int], target: int) -> int:
        # 주어진 list에서 target 값을 넣을 왼쪽 인덱스를 반환
        index = bisect.bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2
solution = Solution()
print(solution.search(nums, target))