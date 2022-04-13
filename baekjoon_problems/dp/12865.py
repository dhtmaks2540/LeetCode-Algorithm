"""
배낭에 넣을 수 있는 물건들의 가치의 최댓값을 출력하라

해당 문제는 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 구하는 문제로
물품과 무게를 iteration하면서 현재 물건을 넣은 경우 최댓값을 갱신하는 방식으로 풀면 된다.
즉, 중복되는 하위 문제를 기록하기 위해서 짐의 개수에 따른 배낭의 용량을 기록하는 테이블을 
사용하면 된다. 점화식은 현재 물건을 넣을 수 있는 경우 현재 물건의 가치 + 이전의 짐을
넣은 가치들 중 현재 짐의 무게를 뺀 가치를 더한 값과 이전의 짐을 넣은 가치들 중 현재 무게의 가치
중 최댓값을 구하는 식이므로 dp[i][j] = max(현재 짐의 가치 + 이전의 짐을 넣은 가치들 중 현재 짐의 무게를 뺀 가치,
이전의 짐을 넣은 가치들 중 현재 무게의 가치)에 해당한다. 그리고 짐을 넣을 수 없는 경우는
이전의 짐을 넣은 가치들 중 현재 무게의 값을 그대로 가져오면 된다.

동전 문제와 굉장히 유사하다고 생각한다.
"""

import sys

def solution():
    # 물품의 수, 버틸 수 있는 무게
    N, K = map(int, sys.stdin.readline().split(" "))
    # 물건의 무게, 물건의 가치
    cargo = []
    for i in range(N):
        capacity, price = map(int, sys.stdin.readline().split(" "))
        cargo.append((capacity, price))
        
    # 짐의 개수, 배낭 용량를 기록하는 테이블
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    # 물품 iteration
    for i in range(1, N + 1):
        # 무게 iteration
        for j in range(1, K + 1):
            # 물품을 실을 수 있을 때
            if cargo[i - 1][0] <= j:
                # 점화식
                # 현재 짐의 가치 + 이전의 짐에서 현재 짐의 무게를 뺀 값의 가치 또는
                # 이전의 짐에서 현재 무게의 가치 중 최댓값
                dp[i][j] = max(
                    cargo[i - 1][1] + dp[i - 1][j - cargo[i - 1][0]],
                    dp[i - 1][j]
                )
            # 실을 수 없을 때
            else:
                dp[i][j] = (dp[i - 1][j])
                
    print(dp[N][K])
    
solution()