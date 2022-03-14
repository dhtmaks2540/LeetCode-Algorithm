from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 정렬 수행
        nums.sort()

        result = 0

        # 두 칸씩 건너뛰면서 더해주기
        # for i in range(0, len(nums), 2):
        #     result += nums[i]

        # 두 칸씩 건너뛰면서 더해주기
        for i, num in enumerate(nums):
            if i % 2 == 0:
                result += num

        return result

    # 파이썬 다운 방식(슬라이싱을 이용)
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    # 페어짝을 이용하여 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

nums = [1,4,3,2]
solution = Solution()
print(solution.arrayPairSum(nums))