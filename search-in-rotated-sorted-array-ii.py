from typing import List

"""
문제 자체가 왜 꼭 이진 탐색을 쓰는건지 이해가 안감
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False

    def search(self, nums: List[int], target: int) -> bool:
        answer = True

        # 비트 연산 사용(같은 값은 남음)
        check_set = set(nums) & set([target])

        if check_set == set():
            answer = False

        return answer

    """
    https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)

    1) everytime check if target == nums[mid], if so, we find it.
    2) otherwise, we check if the first half is in order (i.e. nums[left]<=nums[mid]) 
    and if so, go to step 3), otherwise, the second half is in order,   go to step 4)
    3) check if target in the range of [left, mid-1] (i.e. nums[left] <= target < nums[mid]), if so, do search in the first half, i.e. right = mid-1; otherwise, search in the second half left = mid+1;
    4) check if target in the range of [mid+1, right] (i.e. nums[mid] < target <= nums[right]), if so, do search in the second half, i.e. left = mid+1; otherwise search in the first half right = mid-1;
    
    The only difference is that due to the existence of duplicates, we can have nums[left] == nums[mid] and in that case, 
    the first half could be out of order (i.e. NOT in the ascending order, e.g. [3 1 2 3 3 3 3]) 
    and we have to deal this case separately. In that case, it is guaranteed that nums[right] also equals to nums[mid], 
    so what we can do is to check if nums[mid] == nums[left] == nums[right] before the original logic, 
    and if so, we can move left and right both towards the middle by 1. and repeat.
    """
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            # the only difference from the first one, trickly case, just update left and right
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

    """
    https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).
    """
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target
        
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
solution = Solution()
print(solution.search(nums, target))