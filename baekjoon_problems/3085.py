"""
사탕의 색이 다른 인접한 두 칸을 고른 후, 고른 칸에 들어있는 사탕을 서로 교환한다.
이제 모두 같은 색으로 이루어져있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 먹을 수 있는 사탕의
최대 개수

https://jaimemin.tistory.com/1068

처음 접근은 좌우와 위아래로 값이 다르면 변경 후 DFS를 통해 탐색하려고함.
다만 코드를 구현하지 못해서 해답을 본 결과 단지 변경 후 양옆과 위아래로 최댓값을 판단한 후 
반환하는 방식으로 풀이하면 됐다...

구현은 문제의 조건을 코드로 구현하는 것이 핵심 포인트이다. DFS로 접근했다가 안되면 
하나하나 계산하는 방식으로 생각을 해야하는데 그냥 포기해버린 것이 문제라고 생각한다.
오래 걸리더라도 코드로 생각을 표현하자..!
"""

import sys

sys.stdin = open("input.txt", "rt")

# 보드의 크기
N = int(input())
# 사탕의 색상
graph = []

for _ in range(N):
    graph.append(list(input()))

result = 0

def count_candy():
    result = 1

    # 양 옆
    for i in range(N):
        temp = 1
        for j in range(1, N):
            # 값이 같다면
            if graph[i][j-1] == graph[i][j]:
                temp += 1
            # 값이 다르다면 기록 후 temp 초기화
            else:
                result = max(result, temp)
                temp = 1
        # 양옆을 탐색한 결과 기록
        result = max(result, temp)

    # 위아래
    for i in range(N):
        temp = 1
        for j in range(N - 1):
            # 값이 같다면
            if graph[j + 1][i] == graph[j][i]:
                temp += 1
            # 값이 다르다면 기록 후 temp 초기화
            else:
                result = max(result, temp)
                temp = 1
        # 위아래를 탐색한 결과 기록
        result = max(result, temp)

    return result

for i in range(N):
    for j in range(N):
        # 위 아래로 다를 경우
        if i != 0 and graph[i-1][j] != graph[i][j]:
            # swap -> 계산 -> 다시 돌아오기
            graph[i-1][j], graph[i][j] = graph[i][j], graph[i-1][j]
            # 계산
            result = max(result, count_candy())
            graph[i-1][j], graph[i][j] = graph[i][j], graph[i-1][j]
        # 양 옆으로 다를 경우
        if j != 0 and graph[i][j-1] != graph[i][j]:
            # swap -> 계산 -> 다시 돌아오기
            graph[i][j-1], graph[i][j] = graph[i][j], graph[i][j-1]
            # 계산
            result = max(result, count_candy())
            graph[i][j-1], graph[i][j] = graph[i][j], graph[i][j-1]

print(result)
