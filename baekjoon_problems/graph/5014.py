"""
F층인 건물에서 S에서 시작해 G층으로 가는 경우 버튼의 수의 최솟값을 출력하라

대표적으로 BFS를 사용해서 탐색을 수행하는 문제이다. S에서(시작값) 시작해 G(목표값)에 도착하는데 누르는
버튼의 수의 최솟값을 출력하는 문제로 visited를 통해 방문을 확인하고 방문하지 않았다면 방문처리하고
큐에 삽입하고 방문했다면 패스하는 방식으로 풀이할 수 있다. 조건으로 방문확인 및 
현재 위치에서 U만큼 올라가거나 D만큼 내려갈 경우 정상 범위(1층부터 최고층인 F층 사이이면)이면을 
같이 추가해서 처리하면 된다.
"""

import sys
import collections

# 건물 층 수, 현재 층 수, 회사 층 수, 위로 가는 층 수, 아래로 가는 층 수
F, S, G, U, D = map(int, sys.stdin.readline().strip().split(" "))
visited = [-1] * (F + 1)

queue = collections.deque()
queue.append(S)
# 시작 위치 방문 처리
visited[S] = 0

while queue:
    now = queue.popleft()
    
    # U를 눌러 올라가는 경우
    if 1 <= now + U <= F and visited[now + U] == -1: # 정상 범위이며 방문하지 않았을 경우
        # 방문처리 및 큐에 삽입
        queue.append(now + U)
        visited[now + U] = visited[now] + 1
    
    # D를 눌러 내려가는 경우
    if 1 <= now - D <= F and visited[now - D] == -1: # 정상 범위이며 방문하지 않았을 경우
        # 방문처리 및 큐에 삽입
        queue.append(now - D)
        visited[now - D] = visited[now] + 1

# 방문하지 못했을 경우
if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])