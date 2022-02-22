from itertools import count
from typing import List


import collections

class Solution:
    # Counter를 활용
    def singleNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        return counts.most_common()[-1][0]

    # XOR를 활용(두 번 등장한 엘리먼트는 모두 0으로 초기화, 한 번만 등장하는 엘리먼트는 그 값을 온전히 보존)
    # 0 ^ 0 = 0
    # 4 ^ 0 = 4
    # 4 ^ 4 = 0
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result

nums = [4,1,2,1,2]
solution = Solution()
print(solution.singleNumber(nums))