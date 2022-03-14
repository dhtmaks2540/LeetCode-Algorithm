import collections

"""
Tribonacci의 정답을 구하라

접근방법

파보나치 함수와 비슷한 문제로 다이나믹 프로그래밍으로 접근하려했다.
우선 최적 부분 구조인지 파악해야 하는데 최적 부분 구조란
현재 문제의 최적의 답은 부분 문제의 최적의 답으로 구성된다는 것이다.

만약 현재 문제가 T5(n=2)라고 한다면 T5 = T2 + T3 + T4가 된다
여기서 T4(n=1)은 T4 = T1 + T2 + T3이 되는데, 이는 T5(현재 문제의 최적의 답)의 T4(부분 문제의 최적의 답)
에 해당한다. 따라서 현재 문제는 최적 부분 구조에 해당한다.

그리고 다이나믹 프로그래밍의 두 번째 조건인 하위 문제의 중복또한 위의 예시를 보면 발생한다.
T5에서 T2, T3의 값이 나왔는데 T4에서도 T2, T3의 값이 나오기 때문이다.
따라서 이를 위해 하위 문제의 중복을 저장해두고 사용하는 다이나믹 프로그래밍으로 문제를 풀이
"""
# T0 = 0, T1 = 1, T2 = 1
# Tn+3 = Tn + Tn+1 + Tn+2
class Solution:
    # 상향식(Bottom-Up) 다이나믹 프로그래밍으로 문제 풀이
    def tribonacci(self, n: int) -> int:
        dp = collections.defaultdict(int)

        # T1, T2 = 1
        dp[1] = dp[2] = 1

        # 반복문을 활용한 상향식 다이나믹 프로그래밍
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

    # 하향식(Top-Down) 다이나믹 프로그래밍으로 문제 풀이
    def tribonacci(self, n: int) -> int:
        dp = collections.defaultdict(int)
        
        # T1, T2 = 1
        dp[1] = dp[2] = 1

        def recursive(n):
            if n <= 2:
                return dp[n]

            if dp[n] != 0:
                return dp[n]

            dp[n] = recursive(n - 1) + recursive(n - 2) + recursive(n - 3)

            return dp[n]

        return recursive(n)

n = 25
solution = Solution()
print(solution.tribonacci(n))