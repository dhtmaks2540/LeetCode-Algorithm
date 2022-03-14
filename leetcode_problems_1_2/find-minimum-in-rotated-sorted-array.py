from typing import List


class Solution:
    # 파이썬 min을 사용
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

    """
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
    """

    # pivot(가장 작은 값의 인덱스)를 이진 탐색을 사용해 찾기
    def findMin(self, nums: List[int]) -> int:
        # left, right
        left, right = 0, len(nums) - 1
        # left가 right보다 작은 동안에
        while left < right:
            # mid
            mid = left + (right - left) // 2
            
            # nums[mid]의 값이 nums[right]보다 크다면
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

nums = [3,4,5,1,2]
solution = Solution()
print(solution.findMin(nums))