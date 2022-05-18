"""
부분수열 중에서 그 수열의 합이 S가 되는 경우의 수를 구하라

직접 더해가며 부분 수열의 값이 S가 되는지 확인하는 방식으로 풀이해야하는데 DFS를 사용하면
쉽게 풀이할 수 있다. DFS를 사용하여 탐색을 수행하면서 종료 조건으로는 현재까지 저장된
리스트에 값이 존재하고 그 리스트의 합이 목표값인 경우 결과 변수에 카운트를 증가시키는 방식으로
풀이했다.
"""

import sys

# 정수의 개수, 목표 정수
N, S = map(int, sys.stdin.readline().strip().split(" "))
# 수열
array = list(map(int, sys.stdin.readline().strip().split(" ")))
answer = 0

def dfs(index, path):
    global answer
    # 리스트에 원소가 존재하며 목표값일 경우
    if path and sum(path) == S:
        answer += 1
        
    for i in range(index, N):
        dfs(i + 1, path + [array[i]])
        
dfs(0, [])
print(answer)