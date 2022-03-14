from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        # 자기 자신을 제외한 왼쪽 값 까지의 곱
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        print(out)

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        # 자기 자신을 제외한 오른쪽 값 까지의 곱
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

nums = [-1,1,0,-3,3]
solution = Solution()
print(solution.productExceptSelf(nums))