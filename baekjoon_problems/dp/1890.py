"""
가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하라

해당 문제는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 갈 수 있는 경로의 개수를 구하는 문제이므로
2차원 리스트의 테이블에 우선 시작점의 값을 1로 준다.
이제 테이블을 순회하며 해당 위치에서 오른쪽 또는 아래쪽으로 움직인 후 현재 위치의 값을 더해주는 방식으로
풀면 된다. 즉 점화식은 현재 위치가 i,j라고 한다면 dp[i][j] += dp[i][j]로 이동할 수 있는 경로의 개수에 해당한다.

핵심은 시작점에서 도착점까지 이동하는 경로이므로 모든 경로를 체크하지 않는 것이 중요하다.

"""

import sys

# 게임판의 크기
N = int(input())
# 게임판
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 값을 기록하기 위한 dp 테이블
dp = [[0] * N for _ in range(N)]
# 시작점 초기화
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 도착점이 아니라면
        if i != N - 1 or j != N - 1:
            # 범위안에 드는 경우
            if 0 <= i + graph[i][j] < N:
                dp[i + graph[i][j]][j] += dp[i][j]
            if 0 <= j + graph[i][j] < N:
                dp[i][j + graph[i][j]] += dp[i][j]
                
print(dp[N-1][N-1])