"""
3차원 그래프에서 탐색을 수행할 수 있는지 묻는 문제로 2차원 그래프에서 DFS 또는 BFS를 사용하여 탐색하는
것에서 3차원으로 넓히는 문제이다. 해당 문제는 상하좌우뿐만 아니라 위와 아래로도 움직일 수 있기에 해당
위치를 탐색의 범위로 넣어두고 DFS 또는 BFS를 수행하면 된다.

현재 문제는 3차원 그래프에서 DFS 또는 BFS를 사용하여 탐색을 수행할 수 있는지 묻는 문제로 3차원 그래프를
선언할 수 있고, 방문처리를 통해 무한루프에 빠지지 않도록 처리하는 것이 중요한 문제인듯하다.

"""


import sys
import collections

# 상자의 가로 칸, 상자의 세로 칸, 쌓아올려지는 상자의 수
M, N, H = map(int, sys.stdin.readline().strip().split(" "))
# 상자
graph = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        data = list(map(int, sys.stdin.readline().strip().split(" ")))
        for k in range(M):
            graph[i][j][k] = data[k]
            
dxyz = [(0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
answer = 0

# 토마토가 모두 익었는지 확인하는 메서드
def check_ripe():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 익지않은 토마토가 있다면
                if graph[i][j][k] == 0:
                    return False
    
    return True

if check_ripe():
    print(answer)
    exit()
    
queue = collections.deque()

# 익은 토마토의 위치를 큐에 모두 삽입
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
                
while queue:
    for _ in range(len(queue)):
        now_x, now_y, now_z = queue.popleft()
        
        # 현재 위치와 연결된 토마토를 확인하며
        for i in range(len(dxyz)):
            next_x, next_y, next_z = now_x + dxyz[i][0], now_y + dxyz[i][1], now_z + dxyz[i][2]
            
            # 현재 위치가 정상범위이며
            if 0 <= next_x < H and 0 <= next_y < N and 0 <= next_z < M:
                # 아직 방문하지 않았다면(아직 익지않은 토마토라면)
                if graph[next_x][next_y][next_z] == 0:
                    # 방문처리 및 큐에 삽입
                    graph[next_x][next_y][next_z] = 1
                    queue.append((next_x, next_y, next_z))
                    
    answer += 1
      
# 토마토가 모두 익었다면
if check_ripe():
    print(answer - 1)
else:
    print(-1)