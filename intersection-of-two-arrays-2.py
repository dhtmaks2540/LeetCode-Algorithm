from typing import List


class Solution:
    # set과 & 연산자를 사용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return nums1 & nums2

    # 이진 탐색을 활용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # 중복 제거
        nums1 = set(nums1)
        # 정렬 수행
        nums2.sort()

        def binary_search(target):
            left, right = 0, len(nums2) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] == target:
                    return nums2[mid]
                elif nums2[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        for num in nums1:
            if binary_search(num) != -1:
                result.append(num)

        return result

    # 투포인터 활용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0

        # 투 포인터 우측으로 이동하며 일치 여부 판별
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


nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersection(nums1, nums2))