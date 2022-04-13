"""
https://lmcoa15.tistory.com/96

상근이가 만들 수 있는 올바른 등식의 수를 구하는 프로그램을 작성하라.

dfs로 접근하려 했으나 경우의 수가 굉장히 많은 것을 파악하고 다이나믹 프로래밍으로 풀려고 했다.
다만 점화식을 도출해내지 못해서 풀이하지 못했다...

해당 문제는 0보다 크거나 같고 20보다 작거나 같은 것이 핵심이다.
점화식을 세울 때, N번째 경우의 수는 
1. N-1번째에 구한 경우의 수에서 다음 숫자를 더했을 때 20보다 작거나 같고
2. 다음 숫자를 뺏을 때 0보다 크거나 같을 때

N - 1번째의 경우의 수를 더해주면 N번째의 경우의 수가 나온다.
"""

import sys

# 숫자의 개수
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(" ")))
# N번째 숫자에서 값(합,차)의 경우의 수
dp = [[0] * 21 for _ in range(101)]
# 시작점(numbers[0])가 되는 경우의 수 = 1
dp[1][numbers[0]] += 1

# 숫자 iterate
for i in range(2, N):
    # 값의 범위 iterate
    for j in range(21):
        # 이전 숫자를 계산한 경우의 수에 값이 있다면
        if dp[i - 1][j]:
            # 현재 값을 더한게 범위안에 있다면 경우의 수 갱신
            if j + numbers[i - 1] <= 20: dp[i][j + numbers[i - 1]] += dp[i - 1][j]
            # 현재 값을 뺀게 범위안에 있다면 경우의 수 갱신
            if j - numbers[i - 1] >= 0: dp[i][j - numbers[i - 1]] += dp[i - 1][j]
            
print(dp[N - 1][numbers[-1]])