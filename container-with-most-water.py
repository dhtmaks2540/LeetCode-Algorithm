from typing import List


class Solution:
    # 브루드 포스로 접근 -> 시간 초과
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0

        for i in range(1, len(height)):
            for j in range(i):
                distance = i - j
                max_volume = max(min(height[i], height[j]) * distance, max_volume)

        return max_volume

    def maxArea(self, height):
        # 왼쪽, 오른쪽 포인터
        i, j = 0, len(height) - 1
        water = 0
        # 오른쪽 포인터가 왼쪽 포인터보다 클 때까지
        while i < j:
            # 값 갱신
            water = max(water, (j - i) * min(height[i], height[j]))
            # 왼쪽 포인터의 값이 오른쪽 포인터의 값보다 작다면
            if height[i] < height[j]:
                i += 1
            else: # 오른쪽 포인터의 값이 왼쪽 포인터보다 작다면
                j -= 1
        return water

    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))