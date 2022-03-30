"""
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 식이 몇 초 후인지
그리고 어떻게 이동해야 하는지 출력하라

숨바꼭질 다른 문제와 비슷하게 방문처리를 통하여 중복되지 않게 계산하는 것은 비슷하지만
최소 시간으로 도착지에 도착했을 때 경로가 필요한 문제이다. 이는 해당 지점을 방문하기
직전에 있던 지점을 parent 배열에 저장해놓은 뒤 역순으로 이를 출력하면 여태까지 방문했던
경로를 쉽게 파악할 수 있다.
"""

import collections

MAX = 100001

# 수빈이의 위치, 동생의 위치
N, K = map(int, input().split())
# BFS 탐색을 위한 큐
queue = collections.deque()
# 방문처리를 확인하기 위한 리스트
visited = [-1] * MAX
# 해당 지점 방문 직전 지점을 저장하기 위한 리스트
trace = [-1] * MAX
# 시작점 방문처리 및 큐에 삽입
visited[N] = 0
queue.append(N)

# 큐에 값이 있는 동안
while queue:
    x = queue.popleft()

    # 현재 위치에서 -1, +1, *2 한 위치를 iterate하며
    for nx in [x + 1, x - 1, x * 2]:
        # 현재 위치가 정상적인 범위안에 들어가며 아직 방문하지 않았다면
        if 0 <= nx < MAX and visited[nx] == -1:
            # 큐에 추가
            queue.append(nx)
            # 방문처리
            visited[nx] = visited[x] + 1
            # 바뀐 지점을 방문하기 전에 현재 지점을 기록
            trace[nx] = x
            # 만약, 값이 같다면 break
            if nx == K: break

answer = []
x = K

# 뒤에서부터 접근
while trace[x] != -1:
    answer.append(x)
    x = trace[x]
# 시작노드 추가
answer += [N]
print(visited[K])
print(*answer[::-1])