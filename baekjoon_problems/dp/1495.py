"""
https://mygumi.tistory.com/145

마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하라. 코인 문제랑 비슷했다고 생각

우선 시작 볼륨부터 곡에 따라 볼륨을 줄이고 높이는 경우의 그래프를 그린다.
그 후 그래프를 따라 내려가다보면 곡이 늘어날수록 경우의 수는 2제곱으로 늘어가지만,
사실상 범위를 벗어나 바꿀 수 없는 경우는 계산할 필요가 없게 된다.

따라서, N번째 곡마다 +- 볼륨으로 바꿀 수 있는지 체크를 하면 된다.
이것을 활용해 점화식을 도출하면 아래와 같다.
dp[N][S] = N번째 곡일 때, 볼륨 S 가능 여부
"""

import sys

# 곡의 개수, 시작 볼륨, 최대 볼륨
N, S, M = map(int, input().split())

def solve():
    # 중복되는 값을 저장하기 위한 리스트
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    # 바꿀 수 있는 볼륨
    array = list(map(int, sys.stdin.readline().split(" ")))
    
    # dp[N][S] = N개 곡에서 볼륨 S 가능 여부
    # 0번째 곡에서 S(시작 볼륨) True로 지정
    dp[0][S] = True
    
    # 곡 순회
    for i in range(1, N + 1):
        # 볼륨 순회
        for j in range(M + 1):
            # 이전의 값이 -1이라면 패스
            if not dp[i - 1][j]:
                continue
            # 현재 볼륨을 뺀 값이 0보다 크다면
            if j - array[i - 1] >= 0:
                dp[i][j - array[i - 1]] = True
            
            # 현재 볼륨을 더한 값이 최댓값을 넘지 않는다면
            if j + array[i - 1] <= M:
                dp[i][j + array[i - 1]] = True
    
    # 거꾸로 순회하면서(최댓값부터 접근)
    for i in range(M, -1, -1):
        # 현재 볼륨을 틀 수 있다면
        if dp[N][i]:
            print(i)
            return
    # 틀 수 없는 경우
    print(-1)
    
solve()