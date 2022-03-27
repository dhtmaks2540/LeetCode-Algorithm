"""
미로가 주어질 때, (1,1) 에서 출발하여 (N, M) 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하라

최소의 칸 수로 이동해야 하기에 현재 위치의 값은 현재 위치의 값과 이전에 인접한 값을 더해주기만 하면 된다.
따라서 BFS를 사용해 현재 노드와 인접한 노드를 탐색하는데 조건으로 현재 노드가 1일 경우에만 queue에 넣어
탐색하는 방식으로 문제를 풀이한다.

우선 시작 노드와 시작 노드의 값을 큐에 삽입하고
BFS 코드이므로 큐에 값이 있는 동안 순회하며
현재 노드의 주변 노드를 방문하는데, 이때 주변 노드가 그래프의 범위 안에 있으며 그 값이 1인 경우에만
더해주면 최소의 경로로 목표 노드까지 달성할 수 있다.
"""

import collections

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
# 현재 위치에서 동서남북 x, y좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
# 시작노드 추가
queue = collections.deque([(0, 0, graph[0][0])])
# 큐에 값이 있는 동안
while queue:
    cur_x, cur_y, cur_point = queue.popleft()
    
    # 동서남북을 확인하면서 범위안에 있으며 그 값이 1인 경우에만 넣기
    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 1:
            graph[next_x][next_y] += cur_point
            queue.append((next_x, next_y, graph[next_x][next_y]))
            
print(graph[N-1][M-1])