from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m과 n이 0보다 큰 동안에
        while m > 0 and n > 0:
            # nums의 m-1 인덱스의 값이 nums2의 n-1 인덱스 값보다 크거나 같다면
            if nums1[m - 1] >= nums2[n - 1]:
                # 마지막 인덱스에 nums1 값 주기
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            # nums의 m-1 인덱스의 값이 nums2의 n-1 인덱스 값보다 작다면
            else:
                # 마지막 인덱스에 nums2 값 주기
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # nums2가 남아있다면
        # nums2 남은 수 모두 처리
        if n > 0:
            nums1[:n] = nums2[:n]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
print(solution.merge(nums1, m, nums2, n))