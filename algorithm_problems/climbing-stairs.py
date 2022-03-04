import collections

class Solution:
    dp = collections.defaultdict(int)
    # 상향식
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        # n이 2보다 작으면 
        if n <= 2:
            return n

        # 1 계단 오르는 방법
        dp[1] = 1
        # 2 계단 오르는 방법
        dp[2] = 2

        for i in range(3, n + 1):
            # 다음 계단을 오르는 방법은
            # 이전의 계단에서 1칸 오르기 + 2개 전의 계단에서 2칸 오르기
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # 메모이제이션
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]


n = 5
solution = Solution()
print(solution.climbStairs(n))