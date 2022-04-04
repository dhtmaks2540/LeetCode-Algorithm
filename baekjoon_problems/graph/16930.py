"""
시작점 (x1, y1)과 도착점 (x2, y2)가 주어졌을 때, 시작점에서 도착점으로 이동하는 최소 시간을 구하라

그래프의 시작점에서 도착점으로 가는 최소 시간을 구하는 문제로 그래프의 탐색과 관련된 대표적인 문제이다.
해당 문제는 조건이 까다로워서 BFS로 그래프를 탐색하였는데 최적화를 하는 것이 문제를 푸는 핵심이다.
최적화 조건을 구현하는 것을 항상 생각하기!
"""

import collections

# 체육관의 크기, 1초에 이동할 수 있는 칸의 최대 개수
N, M, K = map(int, input().split())
# 체육관(.은 빈칸, #은 벽)
graph = [list(input()) for _ in range(N)]
# 시작점, 도착점
sta_x, sta_y, des_x, des_y = map(int, input().split())
# 방문확인을 위한 변수
visited = [[-1] * M for _ in range(N)]
visited[sta_x - 1][sta_y - 1] = 0

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS 탐색을 위한 queue
queue = collections.deque()
# 시작점 넣기
queue.append((sta_x - 1, sta_y - 1))

# 큐에 값이 있는 동안
while queue:
    x, y = queue.popleft()
    
    # 동서남북 최대 k번만큼 이동
    for i in range(4):
        for mul in range(1, K + 1):
            nx = dx[i] * mul + x
            ny = dy[i] * mul + y
            
            # 범위를 벗어나거나 해당 위치가 벽이라면 break
            if not (0 <= nx < N and 0 <= ny < M) or graph[nx][ny] == '#':
                break
            # 해당 위치를 방문했고 이동한 위치가 이동하기전 위치보다 작거나 같다면
            if visited[nx][ny] != -1 and visited[nx][ny] <= visited[x][y]:
                break
            # 해당 위치를 방문했다면 continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
            
if visited[des_x - 1][des_y - 1] == 0:
    print(-1)
else:
    print(visited[des_x - 1][des_y - 1])