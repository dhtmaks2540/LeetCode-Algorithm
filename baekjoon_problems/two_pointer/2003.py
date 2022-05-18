"""
수열에서 연속된 부분 수열의 합이 M이 되는 경우의 수를 출력하라

DFS를 사용해서 문제를 풀이하려고 했는데 연속된 부분 수열을 나타낼 방법을 찾지 못했다... 힌트를 보니
투 포인터를 사용해서 풀이하라고 해서 모든 원소가 양수일 때, 투 포인터를 사용해서 연속된 부분 수열의
합을 확인하는 방법으로 문제를 풀이했다. 모든 원소가 양수일 때 투 포인터를 사용할 수 있는 이유는
시작점과 끝점을 주고 시작점이 증가하면 부분 수열의 합이 감소하고, 끝점이 증가하면 부분 수열의 합이
증가하기 때문에 사용할 수 있는 것이다.

이러한 문제는 직접 부분 수열을 확인하는 방식으로 풀이해야 한다. 그 부분 수열을 확인하기 위해서 완전
탐색을 수행하기 보다는 투 포인터를 이용해서 문제의 시간 복잡도를 줄이는 방식으로 풀이한 것이다!
"""

import sys

# 수의 개수, 목표값
N, M = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))
answer = 0
# 합을 계산하기 위한 변수
interval_sum = 0
# 끝점
end = 0

# 시작점은 차례대로 증가
for start in range(N):
    # 현재 start ~ end의 합이 목표값보다 작고, 끝점이 마지막 인덱스가 되기전까지
    while interval_sum < M and end < N:
        # 끝점 증가시키며 계산
        interval_sum += array[end]
        end += 1
    # 부분합이 M이 되었다면
    if interval_sum == M:
        answer += 1
    # 시작점은 iteration하므로 마지막에 시작점의 값 빼기
    interval_sum -= array[start]

print(answer)