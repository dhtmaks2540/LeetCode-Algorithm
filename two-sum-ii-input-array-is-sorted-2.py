from typing import List
import bisect

class Solution:
    # 이진 검색을 이용하여 문제 풀이
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            temp = target - numbers[i]

            left, right = i + 1, len(numbers) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if mid != i and numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] > temp:
                    right = mid - 1
                else:
                    left = mid + 1
    
    # 투 포인터를 이용하여 문제 풀이(정렬되어 있기에 가능)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 왼쪽, 오른쪽 포인터
        left, right = 0, len(numbers) - 1

        while not left == right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    # bisect + 슬라이싱 제거
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1

    # dictionary 사용(정렬안된 리스트에도 사용가능)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num] + 1, i + 1]
            dic[num] = i

numbers = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(numbers, target))