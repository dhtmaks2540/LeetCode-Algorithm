"""
파이프가 (1,1), (2,2)를 차지하고 있고 방향은 가로이다. 파이프의 한쪽 끝을 (N,N)으로 이동시키는
방법의 개수를 구하라

DP로 문제를 접근하였는데 사실상 DP가 아닌 DFS와 같은 방법으로 문제를 풀이하였고, 당연히
시간초과가 발생하게 되었다.
"""

# # 시간초과
# def dp():
#     import collections 

#     # def dp():
#     # 집의 크기
#     N = int(input())
#     # 집의 상태(빈 칸은 0, 벽은 1)
#     graph = []
#     for _ in range(N):
#         graph.append(list(map(int, input().split())))

#     dp = [[] for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             dp[i].append([])

#     # 시작점 초기화
#     dp[0][1].append('0')

#     type_dic = {
#         '0': '가로',
#         '1': '세로',
#         '2': '대각선'
#     }

#     def check(type, i, j):
#         if type_dic[type] == '가로':
#             # 가로로 밀기
#             if 0 <= j + 1 < N:
#                 # 오른쪽이 벽이 아니라면
#                 if graph[i][j + 1] != 1:
#                     dp[i][j + 1].append('0')
#             # 대각선으로 밀기
#             if 0 <= i + 1 < N and 0 <= j + 1 < N:
#                 # 세 개의 좌표가 모두 벽이 아니라면
#                 if graph[i][j + 1] != 1 and graph[i + 1][j] != 1 and graph[i + 1][j + 1] != 1:
#                     dp[i + 1][j + 1].append('2')
#         elif type_dic[type] == '세로':
#             # 세로로 밀기
#             if 0 <= i + 1 < N:
#                 # 아래쪽이 벽이 아니라면
#                 if graph[i + 1][j] != 1:
#                     dp[i + 1][j].append('1')
#             # 대각선으로 밀기
#             if 0 <= i + 1 < N and 0 <= j + 1 < N:
#                 if graph[i][j + 1] != 1 and graph[i + 1][j] != 1 and graph[i + 1][j + 1] != 1:
#                     dp[i + 1][j + 1].append('2')
#         elif type_dic[type] == '대각선':
#             # 가로로 밀기
#             if 0 <= j + 1 < N:
#                 # 오른쪽이 벽이 아니라면
#                 if graph[i][j + 1] != 1:
#                     dp[i][j + 1].append('0')
#             # 세로로 밀기
#             if 0 <= i + 1 < N:
#                 # 아래쪽이 벽이 아니라면
#                 if graph[i + 1][j] != 1:
#                     dp[i + 1][j].append('1')
#             # 대각선으로 밀기
#             if 0 <= i + 1 < N and 0 <= j + 1 < N:
#                 if graph[i][j + 1] != 1 and graph[i + 1][j] != 1 and graph[i + 1][j + 1] != 1:
#                     dp[i + 1][j + 1].append('2')

#     for i in range(N):
#         for j in range(N):
#             # 현재 위치에 값이 있다면
#             if dp[i][j]:
#                 for x in dp[i][j]:
#                     check(x, i, j)

#     for x in dp:
#         print(x)

"""
https://buddev.tistory.com/36

파이프를 놓을 수 있는 방법은 3가지(가로, 대각선, 세로) 이다. 따라서 각각의 경우의 수를 저장할 수 있는
3차원 배열을 생성. int[N][N][3] -> [행][열][가로:0,대각선:1,세로:2]

현재 칸을 (x, y)라고 한다면

1. 가로 방향
가로 방향으로 놓을 수 있는 경우는, 이전 파이프를 가로 또는 대각선으로 놓는 경우이다.
즉, [x][y-1] 칸의 [0]번째 값과 [1]번쨰 값을 더한다.

2. 대각선 방향
대각선 방향으로 놓을 수 있는 경우는, 이전 파이프가 뭐든지 상관없이 가로/대각선/세로 일때 모두 가능
즉, [x-1][y-1] 칸의 [0]번째 값과 [1]번째 값, [2]번째 값을 더해주면 된다.

3. 세로 방향
세로 방향으로 놓을 수 있는 경우는, 이전 파이프를 세로 또는 대각선으로 놓은 경우이다.
즉, [x-1][y] 칸의 [1]번째 값과 [2]번째 값을 더해주면 된다.

해당 문제는 DP를 꼭 1차원의 리스트로만 저장할 필요가 없다는 것과
문제에 주어진 규칙을 잘 활용해서 점화식을 뽑아내는 것이 핵심 포인트같다.

DP 테이블은 (i, j) 위치에서 (가로, 대각선, 세로)의 값을 계산하기 위해서 int[N][N][3]과 같이
3차원의 테이블로 만든다. 그 후 처음 파이프는 [0][1]에서 가로 방향으로 놓여있기에
dp[0][1][0]을 1로 초기화한다.

이제 graph를 iteration 하는데 열 같은 경우는 어차피 2열 이상부터 파이프를 설치할 수 있기에
범위를 2,N으로 잡는다.

그 후 조건을 활용하며 현재 위치가 벽인지, 첫 번째 행인지, 내 왼쪽과 위과 벽인지를 체크하면서
dp 테이블에 가로, 세로, 대각선 방향의 값을 더해주면 된다.

dp로 풀 수 있는 이유는 최적 부분 구조와 하위 문제의 중복이 발생한다는 이유인데
우선 최적 부분 구조에 해당하는 이유는 해당 위치의 경우의 수는 해당 위치의 왼쪽, 위, 대각선 방향에서의
경우의 수를 가지고 구하기에 최적 부분 구조에 해당한다. 즉, graph[2][3]을 구한다고 치면
왼쪽(graph[2][2]), 위(graph[1][3]), 대각선(graph[1][2])의 값을 가지고 풀어야 한다. 그리고
graph[2][2]에서도 graph[1][2]를 위쪽의 값으로 사용해 풀기에 하위 문제의 중복이 발생한다.
따라서 dp를 사용해서 문제를 풀이할 수 있는 것이다.
"""

def dp_solution():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # 3차원 배열
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    # 첫 파이프의 값 넣기(0,1 칸에 가로 파이프의 끝이 있다는 의미)
    dp[0][1][0] = 1

    def func_dp():
        for i in range(N):
            # 파이프는 2열부터 놓을 수 있으므로
            for j in range(2, N):
                # 현재 위치가 벽이면 continue
                if graph[i][j] == 1: continue
                # 현재 위치의 가로 방향 계산
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]

                # 첫 번째 행이라면 continue
                if i == 0: continue
                # 현재 위치의 세로 방향 계산
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]

                # 현재 위치의 왼쪽과 위가 벽이라면 continue(대각선)
                if graph[i - 1][j] == 1 or graph[i][j - 1] == 1: continue
                # 현재 위치의 대각선 방향 계산
                dp[i][j][1] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

        return sum(dp[N-1][N-1])

    print(func_dp())

"""
https://pacific-ocean.tistory.com/458

그래프를 주고 (1,1)에서 (N,N)으로 파이프를 이동시킬 수 있는 경우의 수를 출력하는 문제이므로
그래프 탐색을 활용해서 파이프를 이동시키면서 경우의 수를 구할 수 있다.
아래의 방법은 DFS 탐색을 활용하여 문제를 풀이하였는데, 처음 파이프가 (0, 1)에 가로 방향으로
놓여있으므로 해당 위치와 방향을 DFS 메서드의 파라미터로 념거주고
해당 값을 사용해서 방향을 분기한 후 방향에 따라 이동할 수 있는 방향을 재귀호출하여 풀 수 있다.
"""

# dfs를 활용하여 문제 풀이
def dfs_solution():
    def dfs(x, y, direction):
        global count
        
        # 목표값에 도달했다면 count 증가
        if x == N - 1 and y == N - 1: count += 1
        # 가로
        if direction == 0:
            # 가로로 이동 가능하다면
            if y + 1 < N and graph[x][y + 1] == 0:
                dfs(x, y + 1, 0)
            # 대각선으로 이동 가능하다면
            if x + 1 < N and y + 1 < N:
                if graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0:
                    dfs(x + 1, y + 1, 2)
        # 세로
        elif direction == 1:
            # 세로로 이동 가능하다면
            if x + 1 < N and graph[x + 1][y] == 0:
                dfs(x + 1, y, 1)
            # 대각선으로 이동 가능하다면
            if x + 1 < N and y + 1 < N:
                if graph[x][y + 1] == 0 and graph[x + 1][y] == 0 and graph[x + 1][y + 1] == 0:
                    dfs(x + 1, y + 1, 2)
        # 대각선
        elif direction == 2:
            # 가로로 이동 가능하다면
            if y + 1 < N and graph[x][y + 1] == 0:
                dfs(x, y + 1, 0)
            # 세로로 이동 가능하다면
            if x + 1 < N and graph[x + 1][y] == 0:
                dfs(x + 1, y, 1)
            # 대각선으로 이동 가능하다면
            if x + 1 < N and y + 1 < N:
                if graph[x][y + 1] == 0 and graph[x + 1][y] == 0 and graph[x + 1][y + 1] == 0:
                    dfs(x + 1, y + 1, 2)


    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # (0, 1) 좌표 가로(시작점 DFS 호출)
    dfs(0, 1, 0)
    print(count)