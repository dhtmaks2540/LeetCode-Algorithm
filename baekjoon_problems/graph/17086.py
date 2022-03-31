"""
https://baejinsoo.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0/BOJ_17086/
"""

import collections

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# BFS 탐색을 위한 큐
queue = collections.deque()

dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def bfs():
    # 큐에 값이 있는 동안
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(8):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            # 범위안에 들어가고 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                # 큐에 삽입 후 방문처리 및 위치 증가
                queue.append((nx, ny))
                graph[nx][ny] = graph[cur_x][cur_y] + 1
                
for i in range(N):
    for j in range(M):
        # 해당 위치가 상어라면
        if graph[i][j] == 1:
            queue.append((i, j))
            
bfs()

for i in range(N):
    for j in range(M):
        answer = max(answer, graph[i][j])
        
for x in graph:
    print(x)
        
print(answer - 1)