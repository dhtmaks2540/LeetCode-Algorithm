from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 정렬 수행
        nums.sort()

        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            # 왼쪽 포인터와 오른쪽 포인터
            left, right = i + 1, len(nums) - 1
            # 오른쪽 포인터가 더 클떄까지
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # 같으면 바로 리턴
                if sum == target:
                    return sum

                # 차가 더 작은 값을 저장하기
                if abs(sum - target) < abs(result - target):
                    result = sum

                # sum이 목표값보다 작다면 왼쪽 증가
                if sum < target:
                    left += 1
                # sum이 목표값보다 크다면 오른쪽 증가
                elif sum > target:
                    right -= 1

        return result
            

nums = [-1,2,1,-4]
target = 1

solution =  Solution()
print(solution.threeSumClosest(nums, target))