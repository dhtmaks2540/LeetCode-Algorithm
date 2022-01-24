from typing import List
import collections

class Solution:
    # DFS로 접근
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result = []
        max_value = 0

        # 가장 큰 or 연산은 모든 리스트를 or한 값
        for num in nums:
            max_value |= num
        
        # combinations
        def dfs(index, path):
            temp = 0
            # path의 원소들에 or연산 수행
            for value in path:
                temp |= value
            # 그 값이 최댓값과 같다면
            if temp == max_value:
                result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        
        return len(result)

    """ 
    https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution
    """
    # DP로 접근 -> 점화식
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # dp는 subset의 숫자를 의미
        dp = collections.Counter([0])
        # nums 이터레이션
        for num in nums:
            # dp 테이블 이터레이션
            for k, v in list(dp.items()):
                # 키와 현재값 or 연산 수행
                # 결과로 나온 키에 v 추가
                dp[k | num] += v
        return dp[max(dp)]

nums = [3,2,1,5]
solution = Solution()
print(solution.countMaxOrSubsets(nums))

print(2|1)