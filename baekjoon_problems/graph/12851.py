"""
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지
그리고 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하라.

1697번의 숨바꼭질1과 비슷한 문제인데 해당 문제는 가장 빠른 시간으로 찾는 방법이 몇 가지인 즉, 
경우의 수도 같이 출력해줘야 한다. 따라서 BFS로 똑같이 풀지만 해당 문제는 2차원의 리스트를 만들어
첫 번째 원소는 지점에 도착하는 시간과 두 번째 원소는 경우의 수를 기록한다. 단,
해당 지점에 도달할 수 있는 모든 경우의 수를 저장하는 것이 아니라
'가장 빠른 시간'으로 도달하는 경로인 경우에만 저장해야 한다.

BFS나 DFS를 사용하여 그래프를 탐색하는 경우 방문 처리를 무조건 1차원의 리스트로만
사용하는 것이 아니라 이번 문제와 같이 2차원 리스트를 사용할 수도 있다.

https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-12851%EB%B2%88-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%884-Python-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89BFS
"""

import collections

# BFS로 풀이하는데 방문 처리를 pop할 때 처리하고, 방문 확인은 똑같이 인접한 노드를 
# 확인할 때 체크하는 방식으로 풀이
def bfs1():
    MAX = 100001

    answer = 0
    min_sec = 0
    visited = [False] * MAX

    N, K = map(int, input().split())
    # BFS 탐색을 위한 큐
    queue = collections.deque()
    # 현재 노드 큐에 추가 및 방문 처리
    queue.append((N, 0))

    # 큐에 값이 있는 동안
    while queue:
        x, time = queue.popleft()

        # 해당 문제는 같은 경우의 수도 체크해야 하므로 큐에서 pop할 때 방문지점 표시
        visited[x] = True

        ## 이미 목적지에 한번 도달했을 경우
        if min_sec and min_sec == time and x == K:
            answer += 1
        
        # 최초로 목적지 도달시 최소 시간 기록하고 answer++
        if not min_sec and x == K:
            min_sec = time
            answer += 1

        # 세 가지 경우의 수
        for nx in [x * 2, x + 1, x - 1]:
            if 0 <= nx < MAX and not visited[nx]:
                queue.append((nx, time + 1))

    print(min_sec)
    print(answer)

# 수빈이의 위치, 동생의 위치
N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)] # [지점 i에 도달하는데 걸린 시간, 경우의 수]

def bfs(n):
    # BFS 탐색을 위한 큐
    queue = collections.deque([n])
    # 시작점을 도달하는데 걸린 시간은 0, 경우의 수는 1(시작점 초기화)
    visited[n][0] = 0
    visited[n][1] = 1

    # 큐에 값이 있는 동안
    while queue:
        x = queue.popleft()

        # 현재 위치에서 이동하거나 순간이동 한 위치가 범위 안에 있을 경우
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < 100001:
                if visited[nx][0] == -1: # 처음 도달했다면
                    visited[nx][0] = visited[x][0] + 1 # 걸린 시간 저장
                    visited[nx][1] = visited[x][1] # 경우의 수 저장
                    queue.append(nx)

                elif visited[nx][0] == visited[x][0] + 1: # 처음이 아니라면(하지만 최단 시간 이라면):
                    visited[nx][1] += visited[x][1] # 경우의 수 갱신

    print(visited[K][0])
    print(visited[K][1])

bfs(N)