"""
가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾아라.

https://jaimemin.tistory.com/655

문제에서 입력으로 항상 두 개 이상의 섬이 있는 데이터만 주어진다고 했는데 대충 읽어서 못보고
예외상황으로 계속 생각함... 문제를 잘 읽는게 중요하다.

방향은 잘 떠올렸다. 섬을 다른 색으로 칠하고 BFS로 탐색하면서 다른 섬을 만났을 때 누적된
거리를 반환하며 해당 거리가 최소인 값을 결과로 출력하는 방식으로 생각했다. 다만
코드를 제대로 정리하지 못해서 시간 초과가 발생했다..
"""

def solution():
    import sys
    import collections

    sys.setrecursionlimit(10**5)

    # 지도의 크기
    N = int(sys.stdin.readline().strip())
    # 지도
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    INF = sys.maxsize

    # 동서남북 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 섬에 색 칠하기
    def dfs(x, y, color):
        # 방문처리 및 색 지정
        visited[x][y] = True
        graph[x][y] = color
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 정상범위이며
            if 0 <= nx < N and 0 <= ny < N:
                # 1이고 값이 있을 경우
                if graph[nx][ny] and not visited[nx][ny]:
                    dfs(nx, ny, color)

    def bfs(color):
        queue = collections.deque()
        # 해당 섬의 좌표를 다 큐에 넣는다
        for i in range(N):
            for j in range(N):
                if graph[i][j] == color:
                    visited[i][j] = True
                    queue.append((i, j))
                    
        result = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    # 범위 내에 있고
                    if 0 <= nx < N and 0 <= ny < N:
                        # 다른 섬에 도착할 경우 반환
                        if graph[nx][ny] != 0 and graph[nx][ny] != color:
                            return result
                        # 아직 방문하지 않은 바다칸이면 방문했다고 표시 후 큐에 삽입
                        elif graph[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
            result += 1

    # 섬 다른색으로 칠하기
    color = 1
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j, color)
                color += 1
                
    answer = INF

    for i in range(1, color):
        visited = [[False] * N for _ in range(N)]
        answer = min(answer, bfs(i))
        
    print(answer)

"""
https://www.acmicpc.net/source/42338366

똑같이 DFS와 BFS를 사용하여 문제를 풀이하는데 최적화를 통해 시간복잡도를 줄였다.
"""
    
def solution2():
    import sys
    import collections
    
    N = int(sys.stdin.readline().strip())
    graph = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(N)]
    
    # 동서남북
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    Hor = []
    n = 1
    
    # 섬에 다른색 칠하기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                n += 1
                queue = collections.deque([(i, j)])
                graph[i][j] = n
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                            graph[nx][ny] = n
                            queue.append((nx, ny))
    
    #  현재 섬이며 주변에 바다가 있는 위치 찾기             
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                for di, dj in dxy:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == 0:
                        Hor.append((i, j))
                        break
    
    def bfs(x, y):
        visited = [[-1] * N for _ in range(N)]
        n = graph[x][y]
        # BFS를 위한 큐 생성 및 방문처리
        queue = collections.deque()
        queue.append((x, y))
        visited[x][y] = 0
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                # 정상범위이며 방문하지 않았을 경우
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                    # 다른 섬을 만난 경우
                    if graph[nx][ny] != 0 and graph[nx][ny] != n:
                        return visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    min_len = sys.maxsize
    for a, b in Hor:
        min_len = min(min_len, bfs(a, b))
    
    print(min_len)
        
solution2()