from typing import List
import collections

"""
house-robber와 비슷한 문제이지만 집이 원 모양으로 구성되어 있다 -> 즉, 마지막 인덱스는 첫 번째 인덱스와 연결
따라서 0번 인덱스부터 n-2번 인덱스까지 터는 값과 1번 인덱스부터 n-1 인덱스까지 터는 값중 최댓값을 반환하면 됨

house-robber 문제와 굉장히 비슷하다. 다만 문제에서 0번과 n-1 인덱스가 연결되어 있다는 점만 다르므로
이를 조건으로 생각해서 0번부터 n-2까지 털기 또는 1번부터 n-1까지 털기 중 최댓값을 생각해내지 못했다.
조건을 잘 생각해서 그림으로 그려보고 이를 녹여내는것이 중요.
"""

class Solution:

    """
    https://leetcode.com/problems/house-robber-ii/discuss/60044/Good-performance-DP-solution-using-Java
    """

    # 다이나믹 프로그래밍으로 접근(상향식)
    # 0번 인덱스부터 n-2 인덱스까지 터는 값과 1번 인덱스부터 n-1 인덱스까지 터는 방법으로 분리하여
    # 다이나믹 프로그래밍 진행
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 예외처리
        if n == 0: return 0
        if n == 1: return nums[0]

        def rob(start, end):
            # start, end까지의 nums 복사
            numsNew = nums[start:end+1]
            # DP 테이블
            dp = [0] * len(numsNew)

            # 예외처리
            if len(numsNew) == 0: return 0
            if len(numsNew) == 1: return numsNew[0]

            # DP 테이블
            # 첫 번째 집을 터는 방법은 하나
            dp[0] = numsNew[0]
            # 두 번째 집을 터는 방법은 두 집 중 큰값
            dp[1] = max(numsNew[0], numsNew[1])

            for i in range(2, len(numsNew)):
                # 점화식에 해당
                # 현재 집을 털고 두 칸 전의 집을 터는 최대값 또는
                # 한 칸 전의 집을 터는 최댓값 중 최댓값 
                dp[i] = max(dp[i - 2] + numsNew[i], dp[i - 1])

            return dp[len(numsNew) - 1]

        # 0부터 n-2 까지의 집 터는 값 또는 1부터 n-1 까지의 집 터는 값 중 최댓값
        # 즉, 0과 n-1의 인덱스가 연결되어 있기에 아래와 같이 두 개로 분류하여 문제 풀이
        return max(rob(0, n - 2), rob(1, n - 1))

    """
    https://leetcode.com/problems/house-robber-ii/discuss/59921/9-lines-0ms-O(1)-Space-C%2B%2B-solution
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # 예외처리
        if n == 0: return 0
        if n == 1: return nums[0]

        def robber(l, r):
            # pre는 이전값, cur은 현재 최댓값
            pre, cur = 0, 0
            for i in range(l, r + 1):
                # 갱신
                temp = max(pre + nums[i], cur)
                pre = cur
                cur = temp

            return cur

        # 0번부터 n-2 집까지 털기 또는 1번부터 n-1 집까지 털기 중 최댓값
        return max(robber(0, n - 2), robber(1, n - 1))
    
nums = [2,3,2]
nums = [1,2,3,1]
solution = Solution()
print(solution.rob(nums))