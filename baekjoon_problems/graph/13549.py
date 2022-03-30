"""
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지

BFS를 활용하여 문제를 풀었다. 해당 위치에서 *2, +1, -1한 값이 범위안에 포함되고 아직 방문하지
않았다면 차레대로 큐에 넣고 빼면서 동생과의 위치가 같을 경우 결과값이 되므로 반환하는 방식으로 풀이
queue를 이용하여 BFS로 풀이하는 것이 이 문제의 핵심이다.
"""

import collections

# 수빈이의 위치, 동생의 위치
N, K = map(int, input().split())
# BFS 탐색을 위한 큐
queue = collections.deque()
# 방문을 확인하기 위한 리스트(시간과 경우의 수)
visited = [False] * 100001
# 시작점 추가 및 방문처리
queue.append((N, 0))
visited[N] = True

# 큐에 값이 있는 동안
while queue:
    x, time = queue.popleft()

    # 만약 현재 위치가 동생의 위치와 같다면 반환
    if x == K:
        print(time)
        exit()
    
    # 현재 위치에서 *2한 값이 범위안에 포함되고 방문하지 않았다면
    # 곱하기를 먼저 체크해서 더 빠르게 만들기
    if 0 <= x * 2 < 100001 and not visited[x * 2]:
        # 방문처리 및 큐에 삽입
        visited[x * 2] = True
        queue.append((x * 2, time))

    # 현재 위치에서 -1, +1 범위안에 포함되고 방문하지 않았다면
    for dx in [x - 1, x + 1]:
        if 0 <= dx < 100001 and not visited[dx]:
            # 방문처리 및 큐에 삽입
            visited[dx] = True
            queue.append((dx, time + 1))