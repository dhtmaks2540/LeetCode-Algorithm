"""
(N * M) 크기의 행렬 A와 (M * K) 크기의 행렬 B가 주여졌을 때, 두 행렬을 곱하라

(N * M) 크기의 행렬과 (M * K) 크기의 행렬을 곱하면 일단 결과로 (N * K) 크기의 행렬이 나온다. 이를
브루트 포스로 풀이하면 총 O(N * K * M)의 시간 복잡도가 걸린다. 현재 문제에서는 N과 M 그리고 K가 최대
100이므로 시간 제한 1초안에 아래의 방법으로 풀이할 수 있다.
"""

import sys

# 브루트 포스로 주어진 행렬 곱하기
def solution1():
    # 행렬 A의 크기
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    # 행렬 A
    a_graph = []
    for _ in range(N):
        a_graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        
    # 행렬 B의 크기
    M, K = map(int, sys.stdin.readline().strip().split(" "))
    # 행렬 B
    b_graph = []
    for _ in range(M):
        b_graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        
    result_graph = [[0] * K for _ in range(N)]

    # 행렬 계산
    for i in range(N):
        for j in range(K):
            now_value = 0
            for z in range(M):
                now_value += a_graph[i][z] * b_graph[z][j]
            result_graph[i][j] = now_value

    # 계산 후 결과 출력
    for values in result_graph:
        for value in values:
            print(value, end=" ")
        print()

solution1()