from typing import List
import collections

# 1과 0으로 이루어진 nums에서 0을 k번 바꾼 경우 가장 긴 1의 substring
class Solution:
    # 투포인터, 슬라이딩 윈도우, counter를 활용
    # 최종 목표는 오른쪽 포인터는 크게, 왼쪽 포인터는 작게 하는 것이 목표
    def longestOnes(self, nums: List[int], k: int) -> int:
        # max value, left pointer
        maxf = i = 0
        # record 1, 0's frequency
        counts = collections.Counter()
        # right pointer
        for j in range(len(nums)):
            counts[nums[j]] += 1
            # 1의 최대길이를 찾아야 하므로
            if nums[j] == 1:
                maxf = max(maxf, counts[nums[j]])
            
            # 범위를 벗어난다면(1의 최대 개수 + 변경할 수 있는 개수) left 포안터 줄이기
            if j - i + 1 > maxf + k:
                counts[nums[i]] -= 1
                i += 1
                
        return len(nums) - i

    """
    https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window
    
    슬라이딩 윈도우를 이용하여 풀이

    For each nums[j], try to find the longest subarray
    If nums[i] ~ nums[j] has zeros <= k, we continue to increment j.
    If nums[i] ~ nums[j] has zeros > k, we increment i(as well as j).

    최종 목표는 i는 크게, j는 작게
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            # 현재의 값 빼기(0이면 k 1 감소, 1이면 그대로)
            k -= 1 - nums[j]
            # k가 범위를 벗어난다면
            if k < 0:
                # 왼쪽 슬라이딩 윈도우 이동
                k += 1 - nums[i]
                i += 1

        return j - i + 1


nums = [0,0,0,0]
k = 0
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
solution = Solution()
print(solution.longestOnes(nums, k))