"""
음식물 중 가장 큰 음식물의 크기를 출력하라.

DFS를 활용하여 문제 풀이

그래프를 탐색하는 문제로 현재 위치에서 깊이 우선 탐색으로 조건에 맞는 경우 탐색을 하도록 풀이한다.
우선 해당 위치에 쓰레기가 존재한다면(그래프 상에서 해당 위치가 1이라면)
해당 위치를 기준으로 DFS를 호출하는데 조건으로 좌표가 범위안에 들어가며 값이 1인 경우에만
탐색하도록 한다. 탐색을 시작하면 해당 위치를 방문처리하고, 동서남북으로 재귀호출하면서
해당 위치가 쓰레기인 곳을 더해주면 된다.
"""

# DFS로 문제 풀이
def dfs():
    import sys
    sys.setrecursionlimit(100000)

    # 통로의 길이, 가로 길이, 음식물 쓰레기의 개수
    N, M, K = map(int, input().split())
    # 음식물 쓰레기의 좌표(1은 음식물, 0은 음식물 X)
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1

    # 결과변수
    answer = 0
        
    def dfs(x, y, count):
        # 범위안에 들어가며 해당 위치가 1일 경우
        if 0 <= x < N and 0 <= y < M and graph[x][y] == 1:
            # 방문처리
            graph[x][y] = 2
            count += 1
            
            # 동서남북 방문처리
            count += dfs(x - 1, y, 0)
            count += dfs(x + 1, y, 0)
            count += dfs(x, y - 1, 0)
            count += dfs(x, y + 1, 0)
            
            return count
        # 그 외의 경우 0 반환
        else:
            return 0
        
    for i in range(N):
        for j in range(M):
            # 해당 위치가 음식물 쓰레기 일 경우 DFS 호출
            if graph[i][j] == 1:
                answer = max(answer, dfs(i, j, 0))

    print(answer)

# BFS를 활용하여 문제 풀이
import collections

# 통로의 길이, 가로 길이, 음식물 쓰레기의 개수
N, M, K = map(int, input().split())
# 음식물 쓰레기의 좌표(1은 음식물, 0은 음식물 X)
graph = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

# 동서남북을 나타내는 x, y 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 결과변수
answer = 0
  
def bfs(x, y, count):
    # BFS 탐색을 위한 queue 선언 및 시작노드 추가
    queue = collections.deque([(x, y)])
    # 방문처리
    graph[x][y] = 2
    
    # 큐에 값이 있는 동안에
    while queue:
        cur_x, cur_y = queue.popleft()
        
        # 주변에 연결된 노드를 확인하며
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            # 범위 안에 들어서며 해당 위치에 쓰레기가 있다면
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                # 방문처리 및 쓰레기 추가 후 queue에 추가
                graph[nx][ny] = 2
                count += 1
                queue.append((nx, ny))
                
    return count
                
# 그래프를 순회하며 해당 위치가 쓰레기인 경우 BFS 탐색 호출
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j, 1))
            
print(answer)