"""
대표적인 그래프 탐색 문제이다. 2차원 그래프가 주어지며 현재 위치에서 상하좌우 방향으로 같은 값을
가진 위치를 탐색하기 위해서 DFS 또는 BFS를 사용할 수 있다. 우선 현재 문제에서는 배추가 심어져 있는
총 땅의 개수를 파악하면 된다. 이를 위해서 연결된 배추들은 하나의 땅으로 여겨야 하는데 DFS를 사용해서
현재 위치를 방문처리하고 상하좌우에 배추땅이 있으면 재귀적으로 계속해서 방문처리를 해주면 된다.

2차원 리스트에서 DFS 또는 BFS를 사용하여 그래프를 탐색할 수 있는지 묻는 문제이다. 
"""

import sys
sys.setrecursionlimit(10**5)

# 테스트 케이스
T = int(sys.stdin.readline().strip())
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    global M
    global N
    
    # 현재 위치 방문 처리
    graph[x][y] = 2
    
    # 주변 확인
    for i in range(4):
        next_x, next_y = x + dxy[i][0], y + dxy[i][1]
        # 현재 위치가 정상적인 범위이며 배추밭이라면(방문하지 않았다면)
        if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 1:
            dfs(next_x, next_y)

for _ in range(T):
    # 배추밭의 가로길이, 세로길이, 배추 개수
    M, N, K = map(int, sys.stdin.readline().strip().split(" "))
    
    graph = [[0] * (M) for _ in range(N)]
    # 배추 표시
    for _ in range(K):
        col, row = map(int, sys.stdin.readline().strip().split(" "))
        graph[row][col] = 1
        
    answer = 0
    
    for x in range(N):
        for y in range(M):
            # 현재 위치가 배추라면
            if graph[x][y] == 1:
                dfs(x, y)
                answer += 1
                
    print(answer)