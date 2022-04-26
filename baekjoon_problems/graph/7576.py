"""
며칠이 지나면 토마토들이 모두 익는지 그 최소 일수를 구하라.

BFS를 사용하여 그래프를 탐색하는 방식으로 풀 수 있는 문제이다. 해당 문제를 BFS로 탐색하면
처음 익은 토마토의 위치를 파악해 큐에 삽입한 후, 큐에 값이 들어있는 만큼 동서남북 방향으로 방문처리를
하면 동시간에 방문처리를 처리할 수 있다. 따라서 BFS를 통해서 탐색하며 처음에 모두 익었는지, 탐색을
완료한 후 모두 익었는지 확인해서 정답을 출력하면 된다.

"""

import sys
import collections

# 토마토가 모두 익었는지 확인하는 메서드
def check_ripe():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    
    return True
    
# 가로 칸의 수, 세로 칸의 수
M, N = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

answer = 0

# 처음에 모두 익었는지 확인
if check_ripe():
    print(answer)
    exit()
    
queue = collections.deque()

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 현재 익은 토마토의 위치를 queue에 삽입
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            
# BFS 탐색
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 정상범위이며, 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    # 방문처리 및 큐에 삽입
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
    answer += 1
            
if check_ripe():
    print(answer - 1)
else:
    print(-1)