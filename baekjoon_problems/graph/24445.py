"""
24444번 문제와 똑같지만 단지 내림차순 순서로 방문해야 하므로, 정렬을
수행할 때 내림차순으로 진행한다.

"""

import sys
import collections

# 정점의 수, 간선의 수, 시작 정점
N, M, R = map(int, sys.stdin.readline().strip().split(" "))
# 간선을 기록하기 위한 변수
graph = [[] for _ in range(N + 1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append(end)
    graph[end].append(start)
    
# 내림차순으로 방문하기 위한 정렬 수행
for i in range(N + 1):
    graph[i].sort(reverse=True)
    
queue = collections.deque()
# 방문확인 및 방문순서를 저장하기 위한 변수
answer = [0] * (N + 1)
# 방문 순서를 저장하기 위한 변수
rank = 1

# 시작 정점 방문 처리 및 큐에 삽입
answer[R] = rank
queue.append(R)

# 큐에 값이 있는 동안
while queue:
    now_node = queue.popleft()
    
    # 현재 노드와 연결된 다음 노드 확인
    for next_node in graph[now_node]:
        # 다음 노드를 아직 방문하지 않았다면
        if not answer[next_node]:
            # 순서 기록 및 큐에 삽입
            rank += 1
            answer[next_node] = rank
            queue.append(next_node)
            
for i in range(1, N + 1):
    print(answer[i])