"""
(1,1)에서 출발하여 (N,M)에 이동하기 위해 벽을 최소 몇개 부수어야 하는지

문제를 처음에는 DFS를 사용하여 풀이하려고 했다. 현재 위치에서 동서남북으로 움직일 수 있으며
최소 몇 개의 벽을 지나가야 하는지 체크하는 것이기에 visited 배열을 선언하고 DFS이기에 깊이 우선 탐색
을 수행한다. 따라서 한 경로로 이동하며 현재 위치가 벽이라면 이전의 값에 1을 더하고, 현재 위치가
벽이 아니라면 이전의 값을 그대로 가져오도록 했다. 그러다가 목표 지점에 도달하면 그 값을 갱신하고, 반환하며
해당 위치의 탐색이 끝나면 visited를 다시 -1로 처리하여 방문하지 않도록 한다. 하지만
이와 같이 풀이하니 시간이 너무 오래 걸렸다. 그래서 힌트를 보다보니 우선순위큐를 사용했다는 질문을
보고 BFS와 우선순위큐를 사용하면 현재의 위치 값이 더 작은 쪽을 먼저 방문할테니 더 나은 방식으로
풀이할 수 있을듯 했다. 

방문을 확인하기 위한 리스트와 우선순위 큐를 사용하며 시작점의 값과 좌표를 기록한다. 시작점은 벽이
무조건 아니라고 했으므로 0의 값을 넣고, 동서남북을 탐색하며 다음 좌표가 벽이라면 위의 풀이와 똑같이
이전의 위치에서 1을 더하고, 벽이 아니라면 이전의 위치 값을 그대로 가져오도록 했다. 그리고 그 값을
다시 우선순위 큐에 추가하고 방문처리를 하여 더 벽을 안부수는쪽으로 이동하도록 풀이했다.
"""

import sys
import heapq

# 가로, 세로
M, N = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
visited = [[False] * M for _ in range(N)]

queue = []
heapq.heappush(queue, (0, 0, 0))
visited[0][0] = True
direction_xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    cnt, row, col = heapq.heappop(queue)
    
    for i in range(4):
        next_row, next_col = row + direction_xy[i][0], col + direction_xy[i][1]
        
        # 정상 범위이며 방문하지 않았다면
        if 0 <= next_row < N and 0 <= next_col < M and not visited[next_row][next_col]:
            # 방문 처리
            visited[next_row][next_col] = True
            # 현재 위치가 벽이라면 이전의 값에 1 추가
            if graph[next_row][next_col] == 1:
                graph[next_row][next_col] = cnt + 1
            # 현재 위치가 벽이 아니라면 이전의 값 그대로 가져오기
            else:
                graph[next_row][next_col] = cnt
            
            heapq.heappush(queue, (graph[next_row][next_col], next_row, next_col))
            
print(graph[N - 1][M - 1])