# top-left corner에서 bottom-right conner로 가는 unique path의 합을 구하라
# 로봇은 아래 또는 오른쪽으로 이동 가능

"""
접근방법

2차원 리스트형태의 DP 문제 중 기본에 해당하는 문제라고 생각한다.

왜 DP로 접근했냐하면 유일한 path를 기록하는데 이전의 path가 필요하기에 기록해야 한다고 생각함 -> DP를 통해 기록
목적지(bottom-right) corner로 가는 경로는 로봇의 움직임에 따라서
위에서 아래로 내려가거나 왼쪽에서 오른쪽으로 이동하는 경로뿐이다.
따라서 이전의 값은 생각하지 않고 목적지 dp[row][column] = dp[row - 1][column](왼쪽에서 오른쪽) + dp[row][column - 1](위에서 아래로)
라는 점화식이 도출되고 예외로는 첫 번째 행과 첫 번째 열은 단지 왼쪽에서 오른쪽 또는 위에서 아래로 이동하는
한 가지 방법만 존재하므로 이를 먼저 초기화하고 점화식을 사용하여 문제를 풀이

DP는 보텀업 방식과 탑다운 방식 두 가지가 존재한다.
보텀업 방식은 반복문을 이용하여 작은 문제부터 답을 도출하는 것인데, 아래에서 첫 번째와 두 번째 답에 해당
탑다운은 큰 문제를 해결하기 위해 작은 문제를 호출하는 것으로, 아래에서 세 번째 답에 해당

"""
class Solution:
    # DP로 접근
    def uniquePaths(self, m: int, n: int) -> int:
        # dp 테이블(grid의 크기 만큼)
        dp = [[0] * n for _ in range(m)]

        # 첫 번째 행 초기화(첫 번째 행은 오른쪽 이동하는 방법 하나뿐)
        for i in range(n):
            dp[0][i] = 1

        # 첫 번째 열 초기화(첫 번째 열은 아래로 이동하는 방법 하나뿐)
        for i in range(m):
            dp[i][0] = 1

        # 남은 곳들은 위에서 아래로 이동 + 왼쪽에서 오른쪽으로 이동하는 경로 합
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    # DP로 접근(초기에 dp 테이블을 1로 초기화하여 첫 번쨰 행과 첫 번째 열을 따로 초기화 할 필요 X)
    def uniquePaths(self, m: int, n: int) -> int:
        # dp 테이블
        dp = [[1] * n for _ in range(m)]

        # 남은 곳들의 점화식은 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    """
    https://leetcode.com/problems/unique-paths/discuss/182143/Recursive-memoization-and-dynamic-programming-solutions
    """

    # DP(Memorization) 
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsHelper(m, n, memo):
            # exit condition(범위 내에서만 처리)
            if m < 0 or n < 0:
                return 0
            # 첫 번째 행 또는 첫 번째 열
            elif m == 0 or n == 0:
                return 1
            # 이미 값이 있다면 return
            elif memo[m][n] > 0:
                return memo[m][n]
            else:
                # 현재 위치는 위에서 아래로 내려오는 경로 + 왼쪽에서 오른쪽으로 오는 경로
                memo[m][n] = uniquePathsHelper(m - 1, n, memo) + uniquePathsHelper(m, n - 1, memo)
                return memo[m][n]

        memo = [[0] * n for _ in range(m)]

        return uniquePathsHelper(m - 1, n - 1, memo)
    

m = 3
n = 2
solution = Solution()
print(solution.uniquePaths(m, n))