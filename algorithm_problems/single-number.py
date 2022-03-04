from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # XOR 연산을 이용하여 풀이
            # 값이 같으면 False, 다르면 True를 반환하기에
            # 이 원리를 이용해 중복되는 숫자는 제거
            result ^= num

        return result

nums = [2,2,1]
solution = Solution()
print(solution.singleNumber(nums))