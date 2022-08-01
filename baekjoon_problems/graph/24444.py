"""
해당 문제는 graph를 탐색하는 방법 중 하나인 BFS 탐색의 코드를 작성할 수 있는지 묻는 문제이다. BFS 탐색은
DFS 탐색과 더불어 graph를 탐색하는 방법인데, DFS는 재귀구조를 사용해서 탐색하는 반면 BFS는 queue를
사용해서 탐색을 수행한다. 수행방법은 아래와 같고, 무한으로 탐색을 수행하지 않기 위해서 방문했는지 확인하는
변수는 반드시 필요하다.

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
    
# 오름차순으로 방문하기 위한 정렬 수행
for i in range(N):
    graph[i].sort()
    
queue = collections.deque()
# 방문확인 및 방문순서를 저장하기 위한 변수
answer = [-1] * (N + 1)
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
        if answer[next_node] == -1:
            # 순서 기록 및 큐에 삽입
            rank += 1
            answer[next_node] = rank
            queue.append(next_node)
            
for i in range(1, N + 1):
    if answer[i] == -1:
        print("0")
    else:
        print(answer[i])