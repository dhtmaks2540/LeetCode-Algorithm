"""
체스판을 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력하는 문제

현재 칸에서 8 * 8 칸의 체스칸을 만들 수 있을 때 색칠을 시작해서 총 몇 개를 다시칠해야 하는지
기록하며 그 값의 최솟값을 기록하는 방식으로 풀이. 즉, BFS를 사용하여 풀이할 수 있는데
보드 크기의 최댓값이 50이므로 충분히 풀이할 수 있다.

BFS를 사용하지 않고 단지 주어진 범위내에서 탐색을 수행하면서 색을 변경하는 개수를 기록해서
그 값의 최솟값을 출력하는 방식으로 풀이할 수 있다. 즉, 브루트포스 알고리즘을 사용해서도
문제를 풀이할 수 있다.
"""

# BFS를 사용하여 문제풀이
def solution1():
    import sys
    from collections import deque

    # row, col
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().strip()))
        
    queue = deque()

    min_cnt = sys.maxsize
    move_dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def copy_graph(row, col):
        temp_graph = []
        
        for i in range(row, row + 8):
            temp_graph.append(graph[i][col:col+8])
            
        return temp_graph

    # 체스칸을 만들 수 있는 칸을 순회
    for row_index in range(0, N - 8 + 1):
        for col_index in range(0, M - 8 + 1):
            # 방문체크를 위한 리스트
            visited = [[False] * M for _ in range(N)]
            cnt = 0
            # 임시 그래프
            temp_graph = copy_graph(row_index, col_index)
            
            # 원래의 색으로 시작점 추가 및 방문처리
            queue.append((0, 0, temp_graph[0][0]))
            visited[0][0] = True
            
            while queue:
                row, col, now_color = queue.popleft()
                
                for i in range(4):
                    next_row, next_col = row + move_dir[i][0], col + move_dir[i][1]
                    
                    # 정상 범위이며 방문하지 않았다면
                    if 0 <= next_row < 8 and 0 <= next_col < 8 and not visited[next_row][next_col]:
                        # 현재와 같은 색이라면 -> 다시 칠해야 하는 색
                        if temp_graph[next_row][next_col] == now_color:
                            if now_color == 'W':
                                temp_graph[next_row][next_col] = 'B'
                            else:
                                temp_graph[next_row][next_col] = 'W'
                                
                            cnt += 1
                        # 큐에 다음 위치 추가 후 방문처리
                        queue.append((next_row, next_col, temp_graph[next_row][next_col]))
                        visited[next_row][next_col] = True
            
            # 현재 색과 다른 색으로 칠하는 경우를 계산
            cnt = min(cnt, 64 - cnt)
            
            # 최솟값 갱신        
            min_cnt = min(min_cnt, cnt)
            
    print(min_cnt)

# 브루트포스를 사용해서 문제 풀이(https://st-lab.tistory.com/101)
def solution2():
    import sys
    
    global min_cnt
    
    def find(x, y):
        global min_cnt
        end_x = x + 8
        end_y = y + 8
        cnt = 0
        
        # 첫 번째 칸의 색
        color = graph[x][y]
        
        for i in range(x, end_x):
            for j in range(y, end_y):
                # 올바른 색이 아닐 경우 count 증가
                if graph[i][j] != color:
                    cnt += 1
                    
                # 다음 칸은 색이 바뀌므로
                # true -> false, false - > true로 값 변경
                color = not color
            
            color = not color
            
        # 첫 번째 칸을 기준으로 할 때의 색칠 할 개수와
        # 첫 번째 칸의 색의 반대되는 색을 기준으로 할 때의
        # 색칠 할 개수(64 - count) 중 최솟값을 count에 저장
        cnt = min(cnt, 64 - cnt)
        
        # 최솟값 갱신
        min_cnt = min(min_cnt, cnt)
    
    
    min_cnt = sys.maxsize
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    # 흰색, 검은색을 나타내기 위한 Boolean 리스트
    graph = [[False] * M for _ in range(N)]
    
    for i in range(N):
        data = list(sys.stdin.readline().strip())
        for j in range(M):
            # 현재 색이 흰색이라면
            if data[j] == 'W':
                graph[i][j] = True
            else:
                graph[i][j] = False
    
    # 체스판을 만들려면 최소 8칸이 필요하므로 그 범위를 나타냄 
    N_row = N - 7
    M_col = M - 7
    
    for i in range(N_row):
        for j in range(M_col):
            find(i, j)
            
    print(min_cnt)

# solution2()