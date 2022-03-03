from typing import List

# 연속된 1의 최대 길이
class Solution:
    """
    https://leetcode.com/problems/max-consecutive-ones/discuss/96693/Java-4-lines-concise-solution-with-explanation
    
    The idea is to reset maxHere to 0 if we see 0, otherwise increase maxHere by 1.
    
    Example
    110111
    ^ maxHere = 1

    110111
    .^ maxHere = 2

    110111
    ..^ maxHere = 0

    110111
    ...^ maxHere = 1

    110111
    ....^ maxHere = 2

    110111
    .....^ maxHere = 3
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_here = max_freq = 0

        for num in nums:
            # num이 1이라면 현재값 + 1, 0이라면 0으로 초기화
            max_here = max_here + 1 if num == 1 else 0
            max_freq = max(max_freq, max_here)

        return max_freq

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 최대 빈도, 현재 빈도
        max_freq = sum_freq = 0

        for num in nums:
            sum_freq += num
            if num == 0: # reset sum to zero when encounters zeors
                sum_freq = 0
            else:
                max_freq = max(max_freq, sum_freq)

        return max_freq

nums = [1,1,0,1,1,1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))