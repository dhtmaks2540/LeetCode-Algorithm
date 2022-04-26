"""
섬의 개수를 모두 구하라

대표적인 DFS를 사용하는 문제로 DFS를 사용해서 섬의 개수를 파악하면 된다.
해당 문제는 현재 위치가 섬일 경우 DFS를 통해 탐색하면서 정상범위이면서 아직 방문하지 않았을 경우
방문처리를 하고 문제에서 주어진 방향으로 탐색을 계속해서 수행해 나가면서 연결된 땅을 하나의 섬으로
처리하면서 풀이하면 된다.
"""

import sys
sys.setrecursionlimit(100000)

# 대각선과 동서남북
dx = [-1, 1, -1, 1, 0, 0, 1, -1]
dy = [-1, -1, 1, 1, 1, -1, 0, 0]

def dfs(x, y):
    # 정상범위안에 들어갈 경우
    if 0 <= x < h and 0 <= y < w:
        # 현재 방문하지 않았을 경우
        if graph[x][y] == 1:
            # 방문처리 및 동서남북과 대각선 방문
            graph[x][y] = 2
            
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                dfs(nx, ny)

while True:
    # 지도의 너비, 높이
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    if w == 0 and h == 0:
        break
    # 지도
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        
    answer = 0
    
    # 지도 iteration
    for i in range(h):
        for j in range(w):
            # 현재 위치가 섬이라면 탐색 후 섬 개수 증가
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
            
    print(answer)