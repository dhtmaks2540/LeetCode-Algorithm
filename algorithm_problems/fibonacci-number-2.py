import collections

"""
피보나치 함수를 구현하라

접근방법

우선 파보나치 함수는 최적 부분 구조(문제의 해결 방법은 부분 문제애 대한 최적 해결 방법으로 구성된다)
문제이다. 그 이유는 현재 항의 합은 이전 두 항의 합에 해당하기 때문이다(e.g f(5) = f(4) + f(3), f(4) = f(3) + f(2))
그렇다면 최적 부분 구조 문제에 해당하는 다이나믹 프로그래밍, 그리디 알고리즘, 분할 정복으로
접근할 수 있다는 의미인데 파보나치 함수는 중복된 하위 문제들을 갖는다.

f(5) = f(4) + f(3), f(4) = f(3) + f(2)와 같이 값이 계속 중복되기에 이를 위해 중복되는 값은
미리 기록하는 다이나믹 프로그래밍으로 접근할 수 있는 것이다.
"""
class Solution:
    # DP 테이블에 해당
    dp = collections.defaultdict(int)

    # 다이나믹 프로그래밍(상향식 = Bottom-Up = Tabulation)
    def fib(self, n: int) -> int:
        # 이전의 값을 기록하기 위한 리스트(테이블)
        dp = [0] * (31)

        # dp[1], dp[2]은 모두 1에 해당
        dp[1] = 1

        # 반복문을 통해 상향식 다이나믹 프로그래밍 풀이
        for i in range(2, n + 1):
            # 파보나치 함수에 해당
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # 다이나믹 프로그래밍(하향식 = Top-Down = Memoization)
    def fib(self, n: int) -> int:
        dp = [0] * (31)
        # fibo(1)과 fibo(2)는 1
        dp[1] = 1

        def recursive(n):
            if n <= 2:
                return dp[n]

            if dp[n] != 0:
                return dp[n]

            dp[n] = recursive(n - 1) + recursive(n - 2)

            return dp[n]

        return recursive(n)

    # 다이나믹 프로그래밍(하향식 = Top-Down = Memoization)
    def fib(self, n: int) -> int:
        dp = [0] * (31)
        # fibo(1)과 fibo(2)는 1
        dp[1] = 1

        def recursive(n):
            if n <= 2:
                return dp[n]

            if dp[n] != 0:
                return dp[n]

            dp[n] = recursive(n - 1) + recursive(n - 2)

            return dp[n]

        return recursive(n)
    
    # 책의 정답(메모이제이션 - 하향식)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]

    # 책의 정답(두 변수만을 이용해 공간 절약)
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(0, n):
            x, y = y, x + y

        return x


n = 10
solution = Solution()
print(solution.fib(n))