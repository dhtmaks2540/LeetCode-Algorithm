from typing import List
import sys

"""
연속된 subarray 중 가장 큰 값

접근방법

우선 최적 부분 구조인지 파악하자. 최적 부분 구조는 현재 문제의 최적 해결 방법이 부분 문제의
최적 해결 방법으로 구성된는 경우를 의미한다. 이 문제에서 nums[5]에서의 연속된 subarray 중 가장 큰 값은
nums[4]에서의 연속된 subarary 중 가장 큰 값 + 현재의 값 또는 현재의 값과 같이 부분 문제의 값으로
이루어져 있기에 최적 부분 구조에 해당한다.

거기에 하위 문제에 대한 중복은 dp[5]를 구하면 dp[4]를 사용하고 dp[4]를 사용하면 d[3]을 사용하기에
중복이 발생해 다이나믹 프로그래밍으로 분류할 수 있다. 따라서 현재 문제를 다이나믹 프로그래밍으로 푼다면
점화식은 dp[n] = max(dp[i - 1] + nums[i], nums[i])와 같다. 이는 이전 dp 테이블의 값과 현재의 값을 더한 값과
현재의 값만 가져가는 상황 중 최대값을 가져오도록 설정하면 해당 문제의 정답이 된다.
"""

class Solution:
    # 다이나믹 프로그래밍으로 접근(상향식)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # DP 테이블
        dp = [0] * (n)
        
        # 첫 번째 DP 테이블의 값은 첫 번째 원소를 선택했다고 가정
        dp[0] = nums[0]
        
        for i in range(1, n):
            # 점화식
            # DP 테이블에 기록된 이전 값 + 현재 값 또는 현재 값
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            
        return max(dp)
    
    # 책에서의 정답(메모이제이션)
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # 이전 원소의 값이 0보다 크다면 더하고 아니면 현재 원소만 가져가기
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
    
    # 카데인 알고리즘
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
solution = Solution()
print(solution.maxSubArray(nums))