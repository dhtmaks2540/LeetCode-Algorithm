from typing import List

import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 중복되면 안되기에 결과 변수는 set을 이용
        result = set()

        # 중복된 값 제거
        nums1 = set(nums1)
        nums2 = sorted(list(set(nums2)))
        
        # 재귀적으로 이진 탐색
        def binary_search(left, right, target):
            if left > right:
                return -1

            mid = left + (right - left) // 2

            if nums2[mid] > target:
                return binary_search(left, mid - 1, target)
            elif nums2[mid] < target:
                return binary_search(mid + 1, right, target)
            else:
                return mid

        # nums1 이터레이트
        for num in nums1:
            # nums2에 nums1의 값이 있다면
            if binary_search(0, len(nums2) - 1, num) != -1:
                result.add(num)

        return result

    # 브루드포스로 풀이(O^2)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)

        return result

    # 이진 탐색 모듈 활용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and nums2[i2] == n1:
                result.add(n1)

        return result

    # 투 포인터 활용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0

        # 투 포인터로 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

solution = Solution
solution.intersection(nums1, nums2)