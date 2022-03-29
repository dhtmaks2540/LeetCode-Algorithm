"""
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장
빠른 시간이 몇 초 후인지 구하라.

BFS를 활용하여 풀이

현재 위치에서 목표 위치까지 주어진 조건에 맞게 +1,-1,*2 하는 방식으로 이동해서 
최소의 시간에 도착하는게 문제의 조건이다.

따라서 BFS를 활용하여 현재 위치를 큐에 넣고 뺀 후 현재 위치가 목표 위치와 같다면
시간을 출력하고 반환하고 그렇지 않을 경우 +1, -1, *2를 한 값 중 범위안에 들어가며
방문하지 않았다면 큐에 넣고 방문처리 하는 방식으로 풀 수 있다.
즉, 해당 위치에서 인접한 값들을 방문하여야 하므로 큐를 사용하는 BFS 탐색으로 문제를 풀이할 수 있다.
"""

import collections

# 수빈이의 위치, 동생의 위치
N, K = map(int, input().split())
# BFS 탐색을 위한 큐
queue = collections.deque()
queue.append((N, 0))
# 방문 확인을 위한 리스트
visited = [False] * (100001)
# 시작 노드 방문 처리
visited[N] = True
MAX_SIZE = 100001

# 큐에 값이 있는 동안
while queue:
    x, time = queue.popleft()
        
    # 만약 현재 위치가 목표값이라면
    if x == K:
        print(time)
        exit()

    # 현재 값에서 이동하거나 순간이동한 위치가 범위안에 들어가고 방문하지 않았다면
    for nx in [x * 2, x + 1, x - 1]:
        if 0 <= nx < MAX_SIZE and not visited[nx]:
            # 방문처리 후 큐에 삽입
            visited[nx] = True
            queue.append((nx, time + 1))