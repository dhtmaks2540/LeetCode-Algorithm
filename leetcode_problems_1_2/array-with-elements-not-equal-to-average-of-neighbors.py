from typing import List


class Solution:
    """
    https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/discuss/1403927/JavaC%2B%2BPython-Easy-Solution
    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # 정렬 수행
        nums.sort()

        # 2칸씩 건너뛰면서(홀수만 변경)
        # Sort and swap neighbours into small, big, small, big pattern
        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums
    
    """
    https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/discuss/1403946/C%2B%2B-2-approaches-(simple-intuition-with-example-and-diagram)
    """
    # 왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 두번의 for문을 돌며 변경
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n - 1):
            if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        for i in range(n - 2, 0, -1):
            if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return nums

nums = [1,2,3,4,5]
solution = Solution()
print(solution.rearrangeArray(nums))