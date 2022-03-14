from typing import List

class Solution:
    # 피벗 인덱스를 찾는 것이 관건
    def search(self, nums: List[int], target: int) -> int:
        # 인덱스를 함께 기록
        for i in range(len(nums)):
            nums[i] = (nums[i], i)

        # 정렬 수행
        nums.sort()

        # 이진 탐색
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            num, index = nums[mid]

            if num == target:
                return index
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
    """

    # 피벗 인덱스(회전된 인덱스)를 찾는 것이 관건 -> 최솟값을 피벗으로 삼음
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1
        
        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # mid값에서 회전된 값(pivot) 값을 더한 후 모듈 연산
            mid_pivot = (mid + pivot) % len(nums)

            # 실제 비교는 mid_pivot로
            if nums[mid_pivot] == target:
                return mid_pivot
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

nums = [4,5,6,7,0,1,2]
target = 0
nums = [1,3]
target = 3
solution = Solution()
print(solution.search(nums, target))